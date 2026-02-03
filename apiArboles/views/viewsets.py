from rest_framework import viewsets
from ..models import Arbol, Taxonomia
from ..serializers import ArbolSerializer, TaxonomiaSerializer

class ArbolViewSet(viewsets.ModelViewSet):
    queryset = Arbol.objects.all()
    serializer_class = ArbolSerializer

class TaxonomiaViewSet(viewsets.ModelViewSet):
    queryset = Taxonomia.objects.all()
    serializer_class = TaxonomiaSerializer
