from rest_framework import serializers
from ..models import FotoArbol

class FotoArbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoArbol
        fields = ['id', 'imagen', 'descripcion', 'fecha_creacion']