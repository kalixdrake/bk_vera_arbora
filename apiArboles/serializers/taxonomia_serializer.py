from rest_framework import serializers
from ..models import Taxonomia

class TaxonomiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomia
        fields = '__all__'