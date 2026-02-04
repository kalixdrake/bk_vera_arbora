from django.db import models
from .taxonomia_model import Taxonomia

class Arbol(models.Model):
    # Identificación
    
    no_arbol = models.CharField(max_length=50, verbose_name="No. Árbol", null=True, blank=True)
    codigo_distrital = models.CharField(max_length=50, verbose_name="Código Distrital", null=True, blank=True)
    taxonomia = models.ForeignKey(Taxonomia, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Taxonomía")
    
    
    compensaciones_especiales = models.CharField(verbose_name="Compensaciones Especiales", null=True, blank=True)
    presencia_nidos = models.BooleanField(max_length=100, verbose_name="Presencia de Nidos", null=True, blank=True)
    presencia_epifitas = models.CharField(max_length=100, verbose_name="Presencia de Epifitas", null=True, blank=True)
    brinzales_latizales = models.IntegerField(verbose_name="Brinzales y Latizales", null=True, blank=True)
    intereses_patrimoniales = models.CharField(max_length=100, verbose_name="Intereses Patrimoniales, Afectacion urbana", null=True, blank=True)
    nivel_riesgo = models.CharField(max_length=100, verbose_name="Nivel de Riesgo", null=True, blank=True)
    
    # CONCEPTO TECNICO
    ta_tec = models.BooleanField(max_length=100, verbose_name="Tala", null=True, blank=True)
    co_tec = models.BooleanField(max_length=100, verbose_name="Conservar", null=True, blank=True)
    tra_tec = models.BooleanField(max_length=100, verbose_name="Traslado", null=True, blank=True)
    pre_tec = models.BooleanField(max_length=100, verbose_name="Poda de Formacion / Realce", null=True, blank=True)
    pca_tec = models.BooleanField(max_length=100, verbose_name="Poda de formacion / Control de Alturas", null=True, blank=True)
    pac_tec = models.BooleanField(max_length=100, verbose_name="Poda de formacion Aclareo", null=True, blank=True)
    pe_tec = models.BooleanField(max_length=100, verbose_name="Poda de Estabilidad ", null=True, blank=True)
    es_tec = models.BooleanField(max_length=100, verbose_name="Poda de mejoramiento Estructura", null=True, blank=True)
    sa_tec = models.BooleanField(max_length=100, verbose_name="Poda de mejoramiento Sanitaria ", null=True, blank=True)
    pr_tec = models.BooleanField(max_length=100, verbose_name="Poda Radicular", null=True, blank=True)
    te_tec = models.BooleanField(max_length=100, verbose_name="Tratamiento Especial", null=True, blank=True)
    ti_tec = models.BooleanField(max_length=100, verbose_name="Tratamiento Integral", null=True, blank=True)
    
    # Emplazamiento o tipo de zona verde
    sist_circulacion_urbana = models.CharField(max_length=255, verbose_name="Sistema de Circulación Urbana", null=True, blank=True)
    sist_ludico = models.CharField(max_length=255, verbose_name="Sistema Lúdico", null=True, blank=True)
    sist_hidrico_eaab = models.CharField(max_length=255, verbose_name="Sist Hídrico EAAB", null=True, blank=True)
    a_degradadas = models.CharField(max_length=255, verbose_name="A. Degradadas", null=True, blank=True)
    franja_servidumbre = models.CharField(max_length=255, verbose_name="Franja Servidumbre", null=True, blank=True)
    sist_proteccion = models.CharField(max_length=255, verbose_name="Franja de Control Ambiental", null=True, blank=True)
    e_privado = models.CharField(max_length=255, verbose_name="E Privado", null=True, blank=True)
    
    # Ubicación
    barrio = models.CharField(max_length=100, verbose_name="Barrio", null=True, blank=True)
    direccion_visita = models.CharField(max_length=255, verbose_name="Dirección de Visita", null=True, blank=True)
    localizacion_exacta = models.TextField(verbose_name="Localización Exacta", null=True, blank=True)
    
    latitud = models.FloatField(verbose_name="Latitud", null=True, blank=True)
    longitud = models.FloatField(verbose_name="Longitud", null=True, blank=True)
    localidad = models.CharField(max_length=100, verbose_name="Localidad", null=True, blank=True)
    fecha_visita = models.DateTimeField(verbose_name="Fecha de Visita", null=True, blank=True)
    
    # Recibos / Otros
    recibo_pago_evaluacion = models.CharField(max_length=100, verbose_name="Recibo Pago Evaluación", null=True, blank=True)
    valor_recibo = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Valor Recibo", null=True, blank=True)
    chip = models.CharField(max_length=50, verbose_name="CHIP", null=True, blank=True)
    estrato = models.CharField(max_length=10, verbose_name="Estrato", null=True, blank=True)
    conclusion_concepto_tecnico = models.TextField(verbose_name="Conclusión / Concepto Técnico", null=True, blank=True)
    
    #DETALLE DE INTERVENCION POR OBRA
    matricula_inmobiliaria = models.CharField(max_length=100, verbose_name="Matrícula Inmobiliaria", null=True, blank=True)
    objeto_tramite = models.CharField(max_length=255, verbose_name="Objeto del Trámite", null=True, blank=True)
    nombre_proyecto = models.CharField(max_length=255, verbose_name="Nombre Proyecto", null=True, blank=True)
    area_proyecto_m2 = models.FloatField(verbose_name="Área Proyecto (m2)", null=True, blank=True)
    acta_aprobacion_disenos = models.CharField(max_length=100, verbose_name="Acta Aprobación Diseños", null=True, blank=True)
    fecha_acta_aprobacion_disenos = models.DateTimeField(verbose_name="Fecha Acta Aprobación Diseños", null=True, blank=True)
    cantidad_arbolado_propuesto = models.IntegerField(verbose_name="Cantidad Arbolado Propuesto", null=True, blank=True)
    balance_general_proyecto = models.TextField(verbose_name="Balance General Proyecto", null=True, blank=True)

    def __str__(self):
        return f"Árbol {self.no_arbol} - {self.taxonomia}"
    
    class Meta:
        managed = True
        db_table = "tbl_arboles"
