from django.db import models

class Taxonomia(models.Model):
    codigo = models.CharField(max_length=50, verbose_name="Código", unique=True)
    nombre_comun = models.CharField(max_length=255, verbose_name="Nombre Común")
    nombre_cientifico = models.CharField(max_length=255, verbose_name="Nombre Científico")

    class Meta:
        verbose_name = "Taxonomía"
        managed = True
        db_table = "tbl_taxonomia"

    def __str__(self):
        return f"{self.id} {self.codigo} - {self.nombre_comun} - {self.nombre_cientifico}"
