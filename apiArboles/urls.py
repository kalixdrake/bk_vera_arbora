from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArbolViewSet, TaxonomiaViewSet

router = DefaultRouter()
router.register(r'arboles', ArbolViewSet)
router.register(r'taxonomia', TaxonomiaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
