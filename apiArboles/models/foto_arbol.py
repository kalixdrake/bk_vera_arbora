from django.db import models
from .arbol import Arbol

class FotoArbol(models.Model):
    arbol = models.ForeignKey(Arbol, related_name='fotos', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='arboles/fotos/')
    descripcion = models.CharField(max_length=255, verbose_name="Descripción", null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foto de {self.arbol}"
