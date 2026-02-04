from django.db import models
from .arbol_model import Arbol

class EstadoFisico(models.Model):
    
    arbol = models.ForeignKey(Arbol, related_name='estado_fisico_arbol', on_delete=models.CASCADE)
    
    er = models.BooleanField(max_length=100, verbose_name="Excesiva Ramificacion", null=True, blank=True)
    paa = models.BooleanField(max_length=100, verbose_name="Podas Anteriores Antitecnicas", null=True, blank=True)
    pat = models.BooleanField(max_length=100, verbose_name="Podas Anteriores Tecnicas", null=True, blank=True)
    rs = models.BooleanField(max_length=100, verbose_name="Ramas Secas", null=True, blank=True)
    rb = models.BooleanField(max_length=100, verbose_name="Rebrotes", null=True, blank=True)
    ca = models.BooleanField(max_length=100, verbose_name="Copa Asimetrica", null=True, blank=True)
    rp = models.BooleanField(max_length=100, verbose_name="Ramas Pendulares", null=True, blank=True)
    rpc = models.BooleanField(max_length=100, verbose_name="Ramas Peligro Caida", null=True, blank=True)
    ddr = models.BooleanField(max_length=100, verbose_name="Desgarre De Rama", null=True, blank=True)
    des = models.BooleanField(max_length=100, verbose_name="Descope", null=True, blank=True)
    no = models.BooleanField(max_length=100, verbose_name="Normal", null=True, blank=True)    
    
    DENSO = "1 D_Denso"
    MEDIO = "2 M_Medio"
    RALO = "3 R_Ralo"
    MUY_RALO = "4 MR_Muy Ralo"

    DENSIDAD_CHOICES = (
        (DENSO, "1 D_Denso"),
        (MEDIO, "2 M_Medio"),
        (RALO, "3 R_Ralo"),
        (MUY_RALO, "4 MR_Muy Ralo")
    )
    densidad = models.CharField(
        max_length=100,
        verbose_name="Estado Fisico Copa Densidad",
        choices=DENSIDAD_CHOICES,
        null=True, blank=True
        )
    
    BUENO = "1 Bu_Bueno"
    REGULAR = "2 Re_Regular"
    MALO = "3 Ma_Malo"
    
    GENERAL_ESTADO_CHOICES = (
        (BUENO, "1 Bu_Bueno"),
        (REGULAR, "2 Re_Regular"),
        (MALO, "3 Ma_Malo")
    )

    general_estado = models.CharField(
        max_length=100,
        verbose_name="Estado Fisico Copa General (Estado)",
        choices=GENERAL_ESTADO_CHOICES,
        null=True, blank=True
        )
    
    # Estado Físico FUSTE
    b = models.BooleanField(max_length=100, verbose_name="Bifurcado", null=True, blank=True)
    bb = models.BooleanField(max_length=100, verbose_name="Bifurcacion basal", null=True, blank=True)
    b_basales = models.BooleanField(verbose_name="Bifurcaciones Basales", null=True, blank=True)
    horquilla_v = models.BooleanField(verbose_name="Horquilla V", null=True, blank=True)
    horquilla_u = models.BooleanField(verbose_name="Horquilla U", null=True, blank=True)
    to = models.BooleanField(max_length=100, verbose_name="To", null=True, blank=True)
    fr = models.BooleanField(max_length=100, verbose_name="Fuste Recto", null=True, blank=True)
    i = models.BooleanField(max_length=100, verbose_name="Inclinado", null=True, blank=True)
    gdi = models.BooleanField(verbose_name="Grados De Inclinacion", null=True, blank=True)
    mi = models.BooleanField(max_length=100, verbose_name="Muy Inclinado", null=True, blank=True)
    c = models.BooleanField(max_length=100, verbose_name="Compartimentalizado", null=True, blank=True)
    rv = models.BooleanField(max_length=100, verbose_name="Madera Revirada", null=True, blank=True)
    ac = models.BooleanField(max_length=100, verbose_name="Acanalado", null=True, blank=True)
    an_interv = models.BooleanField(max_length=100, verbose_name="Anillado", null=True, blank=True)
    dc = models.BooleanField(max_length=100, verbose_name="Descortezado", null=True, blank=True)
    sb = models.BooleanField(max_length=100, verbose_name="Socabamiento Basal", null=True, blank=True)
    ag_interv = models.BooleanField(max_length=100, verbose_name="Afectacion por Guadañadora", null=True, blank=True)
    po = models.BooleanField(max_length=100, verbose_name="Presencia de Ojetos Extraños", null=True, blank=True)
    pe = models.BooleanField(max_length=100, verbose_name="Presencia de Encerramientos", null=True, blank=True)
    dm_l = models.BooleanField(max_length=100, verbose_name="Daño Mecanico Leve", null=True, blank=True)
    dm_g = models.BooleanField(verbose_name="Daño Mecanico Grave", null=True, blank=True)
    dm_m = models.BooleanField(verbose_name="Daño Mecanico Medio", null=True, blank=True)
    gri = models.BooleanField(verbose_name="Grietas", null=True, blank=True)
    fis = models.BooleanField(max_length=100, verbose_name="Fisura", null=True, blank=True)
    cav = models.BooleanField(max_length=100, verbose_name="Cavidad", null=True, blank=True)
    ap = models.BooleanField(max_length=100, verbose_name="Arquitectura Pobre", null=True, blank=True)
    ci = models.BooleanField(verbose_name="Corteza Incluida", null=True, blank=True)
    
    BUENO = "1 Bu_Bueno"
    REGULAR = "2 Re_Regular"
    MALO = "3 Ma_Malo"
    SUPRIMIDO = "4 Su_Suprimido"
    
    GENERAL_FUSTE_CHOICES = (
        (BUENO, "1 Bu_Bueno"),
        (REGULAR, "2 Re_Regular"),
        (MALO, "3 Ma_Malo"),
        (SUPRIMIDO, "4 Su_Suprimido")
    )
    general_fuste = models.CharField(
        max_length=100,
        verbose_name="Estado Fisico Fuste General",
        choices=GENERAL_FUSTE_CHOICES,
        null=True, blank=True
        )
    
    #Raiz
    RD_RAICES = "1 RD_Raíces Descubiertas"
    PRADR_PODA = "2 PRADR_Poda Raíz Antitécnica dentro del rádio crítico"
    PRT_PODA = "3 PRT_Poda Raíz Técnica"
    NA_NO = "4 Na_No apreciable"
    PRAFR_PODA = "5 PRAFR_Poda Raíz Antitécnica fuera del rádio crítico"
    RES_RAICES = "6 Res_Raices estranguladoras"
    REN_RAICES = "7 REn_Raices entorchadas"
    MON_MONTICULO = "8 Mon_Montículo"

    ESPECIFICO_RAIZ_CHOICES = (
        (RD_RAICES, "1 RD_Raíces Descubiertas"),
        (PRADR_PODA, "2 PRADR_Poda Raíz Antitécnica dentro del rádio crítico"),
        (PRT_PODA, "3 PRT_Poda Raíz Técnica"),
        (NA_NO, "4 Na_No apreciable"),
        (PRAFR_PODA, "5 PRAFR_Poda Raíz Antitécnica fuera del rádio crítico"),
        (RES_RAICES, "6 Res_Raices estranguladoras"),
        (REN_RAICES, "7 REn_Raices entorchadas"),
        (MON_MONTICULO, "8 Mon_Montículo"),
    )
    especifico = models.CharField(
        max_length=100,
        verbose_name="Estado Fisico Raiz Específico",
        choices=ESPECIFICO_RAIZ_CHOICES,
        null=True, blank=True
        )
    
    EI = "1 EI_Espacio Limitado o Insuficiente"
    EJ = "2 EJ_Espacio Justo o Adecuado"
    ES = "3 ES_Espacio Disponible o Suficiente"
    
    ESPACIO_CHOICES =(
        (EI, "1 EI_Espacio Limitado o Insuficiente"),
        (EJ, "2 EJ_Espacio Justo o Adecuado"),
        (ES, "3 ES_Espacio Disponible o Suficiente")
    )
    
    ed_espacio = models.CharField(
        max_length=100,
        verbose_name="Espacio Disponible para el desarrollo radicular",
        choices=ESPACIO_CHOICES,
        null=True, blank=True
        )
    
    
    general_raiz = models.CharField(
        max_length=100,
        verbose_name="Estado Fisico Raiz General",
        choices=GENERAL_ESTADO_CHOICES,
        null=True, blank=True
        )