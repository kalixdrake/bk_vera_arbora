from rest_framework import serializers
from ..models import Arbol, FotoArbol, Taxonomia
import PIL.Image
from PIL.ExifTags import TAGS, GPSTAGS
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils import timezone
import datetime

from .foto_arbol_serializer import FotoArbolSerializer
from .taxonomia_serializer import TaxonomiaSerializer


class ArbolSerializer(serializers.ModelSerializer):
    fotos = FotoArbolSerializer(many=True, read_only=True)
    uploaded_fotos = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )
    taxonomia_detalle = TaxonomiaSerializer(source='taxonomia', read_only=True)
    taxonomia_id = serializers.PrimaryKeyRelatedField(
        queryset=Taxonomia.objects.all(), source='taxonomia', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Arbol
        fields = '__all__'
        extra_kwargs = {
            'latitud': {'required': False},
            'longitud': {'required': False},
            'fecha_visita': {'required': False},
        }

    def get_exif_data(self, image_file):
        """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
        exif_data = {}
        try:
            image = PIL.Image.open(image_file)
            info = image._getexif()
            if info:
                for tag, value in info.items():
                    decoded = TAGS.get(tag, tag)
                    if decoded == "GPSInfo":
                        gps_data = {}
                        for t in value:
                            sub_decoded = GPSTAGS.get(t, t)
                            gps_data[sub_decoded] = value[t]
                        exif_data[decoded] = gps_data
                    else:
                        exif_data[decoded] = value
        except Exception:
            pass
        return exif_data

    def get_lat_lon(self, exif_data):
        """Returns the latitude and longitude, if available, from the provided exif_data"""
        lat = None
        lon = None

        if "GPSInfo" in exif_data:
            gps_info = exif_data["GPSInfo"]

            gps_latitude = gps_info.get("GPSLatitude")
            gps_latitude_ref = gps_info.get("GPSLatitudeRef")
            gps_longitude = gps_info.get("GPSLongitude")
            gps_longitude_ref = gps_info.get("GPSLongitudeRef")

            if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
                lat = self.convert_to_degrees(gps_latitude)
                if gps_latitude_ref != "N":
                    lat = -lat

                lon = self.convert_to_degrees(gps_longitude)
                if gps_longitude_ref != "E":
                    lon = -lon

        return lat, lon

    def  convert_to_degrees(self, value):
        """Helper function to convert the GPS coordinates stored in the EXIF to degrees in float format"""
        d = float(value[0])
        m = float(value[1])
        s = float(value[2])
        return d + (m / 60.0) + (s / 3600.0)

    def get_date_time(self, exif_data):
        """Returns the date and time from the exif data"""
        date_time_str = exif_data.get("DateTimeOriginal")
        if not date_time_str:
             date_time_str = exif_data.get("DateTime")
        
        if date_time_str:
            # Format usually is 'YYYY:MM:DD HH:MM:SS'
            try:
                # Convert to Django DateTime format (YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ])
                # Replacing colons in date part with dashes
                parts = date_time_str.split(' ')
                date_part = parts[0].replace(':', '-')
                time_part = parts[1]
                
                # Parse naive datetime
                naive_dt = datetime.datetime.strptime(f"{date_part} {time_part}", "%Y-%m-%d %H:%M:%S")
                # Make aware
                return timezone.make_aware(naive_dt)
            except:
                return None
        return None

    def create(self, validated_data):
        uploaded_fotos = validated_data.pop('uploaded_fotos', [])
        
        # If lat/lon/date not provided, try to get from first photo
        if uploaded_fotos:
            first_photo = uploaded_fotos[0]
            # Since ImageField in serializer is a file pointer, we can read it.
            # But we should be careful not to consume it if we need to save it later.
            # However, PIL opens it.
            
            # We need to seek(0) after reading or open a copy?
            # InMemoryUploadedFile usually works fine.
            
            exif_data = self.get_exif_data(first_photo)
            lat, lon = self.get_lat_lon(exif_data)
            date_time = self.get_date_time(exif_data)
            
            if lat and 'latitud' not in validated_data:
                validated_data['latitud'] = lat
            if lon and 'longitud' not in validated_data:
                validated_data['longitud'] = lon
            if date_time and 'fecha_visita' not in validated_data:
                validated_data['fecha_visita'] = date_time # Ensure format matches
        
        arbol = Arbol.objects.create(**validated_data)

        for foto in uploaded_fotos:
            FotoArbol.objects.create(arbol=arbol, imagen=foto)

        return arbol

    def update(self, instance, validated_data):
        uploaded_fotos = validated_data.pop('uploaded_fotos', [])
        
        # Update standard fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Add new photos
        for foto in uploaded_fotos:
            FotoArbol.objects.create(arbol=instance, imagen=foto)
            
        return instance
