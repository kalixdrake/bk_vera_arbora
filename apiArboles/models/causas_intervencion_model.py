from django.db import models
from .arbol_model import Arbol

class CausasIntervencion(models.Model):
    
    arbol = models.ForeignKey(Arbol, related_name='causas_intervencion_silvicultural_arbol', on_delete=models.CASCADE)
    
    #Causas de intervencion silvicultural
    zp = models.BooleanField(verbose_name="Zona de Pendiente", null=True, blank=True)
    ma_other = models.BooleanField(verbose_name="Mal anclado", null=True, blank=True)
    iiv = models.BooleanField(verbose_name="Interferencia Infraestructural Vial", null=True, blank=True)
    ie = models.BooleanField(max_length=100, verbose_name="Interferencia Infraestructura con Edificaciones", null=True, blank=True)
    imu = models.BooleanField(verbose_name="Interferencia Infraestructura de mobilirario Ubrano", null=True, blank=True)
    ira = models.BooleanField(verbose_name="Interferencia Redes de acueducto", null=True, blank=True)
    ire = models.BooleanField(verbose_name="Interferencia Redes electricas", null=True, blank=True)
    hx = models.BooleanField(max_length=100, verbose_name="Altura Excesiva para el lugar de siembra", null=True, blank=True)
    pv = models.BooleanField(verbose_name="Peligro de Volcamiento", null=True, blank=True)
    esv = models.BooleanField(max_length=100, verbose_name="Sp Susceptible Volcamiento", null=True, blank=True)
    auai = models.BooleanField(verbose_name="Arbol ubicado en area inundada", null=True, blank=True)
    id_indicador = models.BooleanField(max_length=100, verbose_name="Inadecuado Distanciamiento", null=True, blank=True)
    des_indicador = models.BooleanField(max_length=100, verbose_name="Deficiente Estado Sanitario", null=True, blank=True)
    di = models.BooleanField(verbose_name="Daño a la Infraestructura", null=True, blank=True)
    def_field = models.BooleanField(verbose_name="Deficiente Estado Fisico", null=True, blank=True)
    eie = models.BooleanField(max_length=100, verbose_name="Espacio Insuficiente de Emplazamiento", null=True, blank=True)
    ni = models.BooleanField(verbose_name="No requiere Intervencion", null=True, blank=True)
    
    COP = "5 Cop_Construcción de obra Pública"
    CPR = "6 Cpr_Construcción de obra Privada"
    CAUSAS_CHOICES = (
        (COP, "5 Cop_Construcción de obra Pública"),
        (CPR, "6 Cpr_Construcción de obra Privada")
    )
    causas_int_obra_civil = models.CharField(
        verbose_name="Causas Int Obra Civil",
        choices=CAUSAS_CHOICES,
        null=True, blank=True
        )