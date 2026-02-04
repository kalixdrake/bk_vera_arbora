from django.db import models
from .arbol_model import Arbol

class Dimensiones(models.Model):
    
    arbol = models.ForeignKey(Arbol, related_name='dimensiones_arbol', on_delete=models.CASCADE)
    
    # Dimensiones
    pap_m = models.FloatField(verbose_name="Perimetro a la altura de pecho (m)", null=True, blank=True)
    metro_lineales_seto = models.FloatField(verbose_name="Metros lineales (SETO)", null=True, blank=True)
    alt_tot_m = models.FloatField(verbose_name="Altura Total (m)", null=True, blank=True)
    alt_com_m = models.FloatField(verbose_name="Altura Comercial (m)", null=True, blank=True)
    diam_copa_polar_m = models.FloatField(verbose_name="Diámetro Copa Polar (m)", null=True, blank=True)
    diam_copa_ecuatorial_m = models.FloatField(verbose_name="Diámetro Copa Ecuatorial (m)", null=True, blank=True)
    p_basal_m = models.FloatField(verbose_name="Perimetro Basal (m)", null=True, blank=True)