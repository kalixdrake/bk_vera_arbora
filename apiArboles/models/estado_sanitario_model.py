from django.db import models
from .arbol_model import Arbol

class EstadoSanitario(models.Model):
    
    arbol = models.ForeignKey(Arbol, related_name='estado_sanitario_arbol', on_delete=models.CASCADE)
    
    # Estado sanitario Copa
    he_c = models.BooleanField(verbose_name="Herviboria (Copa)", null=True, blank=True)
    an_c = models.BooleanField(verbose_name="Antracnosis (Copa)", null=True, blank=True)
    ag_c = models.BooleanField(verbose_name="Agallas (Copa)", null=True, blank=True)
    ne_c = models.BooleanField(verbose_name="Necrosis (Copa)", null=True, blank=True)
    tu_c = models.BooleanField(verbose_name="Tumores (Copa)", null=True, blank=True)
    cl_c = models.BooleanField(max_length=100, verbose_name="Clorosis (Copa)", null=True, blank=True)
    ma_c = models.BooleanField(max_length=100, verbose_name="Marchitamiento (Copa)", null=True, blank=True)
    ca_c = models.BooleanField(verbose_name="Cancer (Copa)", null=True, blank=True)
    pl_c = models.BooleanField(verbose_name="Pudricion Localizada (Copa)", null=True, blank=True)
    mi_c = models.BooleanField(verbose_name="Mildeos (Copa)", null=True, blank=True)
    c_c = models.BooleanField(verbose_name="Carbones (Copa)", null=True, blank=True)
    ro_c = models.BooleanField(verbose_name="Royas (Copa)", null=True, blank=True)
    psu_c = models.BooleanField(max_length=100, verbose_name="Puntos de Succión (Copa)", null=True, blank=True)
    pt_c = models.BooleanField(verbose_name="Puntos Traslucidos (Copa)", null=True, blank=True)
    pla_c = models.BooleanField(verbose_name="Plasmolisis (Copa)", null=True, blank=True)
    pi_c = models.BooleanField(max_length=100, verbose_name="Presencia de insectos (Copa)", null=True, blank=True)
    na_c = models.BooleanField(max_length=100, verbose_name="Ninguna de las anteriores (Copa)", null=True, blank=True)
    
    BUENO = "1 Bu_Bueno"
    REGULAR = "2 Re_Regular"
    MALO = "3 Ma_Malo"
    
    GENERAL_ESTADO_CHOICES = (
        (BUENO, "1 Bu_Bueno"),
        (REGULAR, "2 Re_Regular"),
        (MALO, "3 Ma_Malo")
    )
    copa = models.CharField(
        max_length=100,
        verbose_name="Estado sanitario Copa",
        choices=GENERAL_ESTADO_CHOICES,
        null=True, blank=True
        )
    
    # Estado sanitario Fuste
    re_f = models.BooleanField(verbose_name="Resinosis (Fuste)", null=True, blank=True)
    hg_f = models.BooleanField(verbose_name="Hongos (Fuste)", null=True, blank=True)
    ch_f = models.BooleanField(verbose_name="Chancros (Fuste)", null=True, blank=True)
    pl_f = models.BooleanField(verbose_name="Pudricion Localizada (Fuste)", null=True, blank=True)
    go_f = models.BooleanField(verbose_name="Gomosis (Fuste)", null=True, blank=True)
    tu_f = models.BooleanField(verbose_name="Tumores (Fuste)", null=True, blank=True)
    ag_f = models.BooleanField(verbose_name="Agallas (Fuste)", null=True, blank=True)
    pi_f = models.BooleanField(verbose_name="Presencia de insectos (Fuste)", null=True, blank=True)
    na_f = models.BooleanField(max_length=100, verbose_name="Ninguna de las anteriores (Fuste)", null=True, blank=True)
    
    fuste = models.CharField(
        max_length=100,
        verbose_name="Estado sanitario (Fuste)",
        choices=GENERAL_ESTADO_CHOICES,
        null=True, blank=True
        )
    
    # Estado sanitario Raiz
    pl_r = models.BooleanField(verbose_name="Pudricion Localizada (Raiz)", null=True, blank=True)
    na_r = models.BooleanField(max_length=100, verbose_name="Ninguna de las anteriores (Raiz)", null=True, blank=True)
    
    raiz = models.CharField(
        max_length=100,
        verbose_name="Estado sanitario (Raiz)",
        choices=GENERAL_ESTADO_CHOICES,
        null=True, blank=True
        )
    
    #Estado sanitario general
    ps = models.BooleanField(max_length=100, verbose_name="Parcialmente Seco", null=True, blank=True)
    se = models.BooleanField(verbose_name="Seco", null=True, blank=True)
    sa = models.BooleanField(max_length=100, verbose_name="Sano", null=True, blank=True)