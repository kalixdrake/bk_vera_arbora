from django.db import models
from .taxonomia import Taxonomia

class Arbol(models.Model):
    # Identificación
    no_arbol = models.CharField(max_length=50, verbose_name="No. Árbol", null=True, blank=True)
    codigo_distrital = models.CharField(max_length=50, verbose_name="Código Distrital", null=True, blank=True)
    taxonomia = models.ForeignKey(Taxonomia, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Taxonomía")
    
    # Dimensiones
    pap_m = models.FloatField(verbose_name="Perimetro a la altura de pecho (m)", null=True, blank=True)
    metro_lineales_seto = models.FloatField(verbose_name="Metros lineales (SETO)", null=True, blank=True)
    alt_tot_m = models.FloatField(verbose_name="Altura Total (m)", null=True, blank=True)
    alt_com_m = models.FloatField(verbose_name="Altura Comercial (m)", null=True, blank=True)
    diam_copa_polar_m = models.FloatField(verbose_name="Diámetro Copa Polar (m)", null=True, blank=True)
    diam_copa_ecuatorial_m = models.FloatField(verbose_name="Diámetro Copa Ecuatorial (m)", null=True, blank=True)
    p_basal_m = models.FloatField(verbose_name="Perimetro Basal (m)", null=True, blank=True)
    
    # Estado Físico Copa
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
    
    densidad = models.CharField(max_length=100, verbose_name="Estado Fisico Copa Densidad", null=True, blank=True)
    general_estado = models.CharField(max_length=100, verbose_name="Estado Fisico Copa General (Estado)", null=True, blank=True)
    
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
    general_fuste = models.CharField(max_length=100, verbose_name="Estado Fisico Fuste General", null=True, blank=True)
    
    #Raiz
    especifico = models.CharField(max_length=100, verbose_name="Estado Fisico Raiz Específico", null=True, blank=True)
    ed_espacio = models.CharField(max_length=100, verbose_name="Espacio Disponible para el desarrollo radicular", null=True, blank=True)
    general_raiz = models.CharField(max_length=100, verbose_name="Estado Fisico Raiz General", null=True, blank=True)
    
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
    copa = models.CharField(max_length=100, verbose_name="Estado sanitario Copa", null=True, blank=True)
    
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
    fuste = models.CharField(max_length=100, verbose_name="Estado sanitario (Fuste)", null=True, blank=True)
    
    # Estado sanitario Raiz
    pl_r = models.BooleanField(verbose_name="Pudricion Localizada (Raiz)", null=True, blank=True)
    na_r = models.BooleanField(max_length=100, verbose_name="Ninguna de las anteriores (Raiz)", null=True, blank=True)
    raiz = models.CharField(max_length=100, verbose_name="Estado sanitario (Raiz)", null=True, blank=True)
    
    #Estado sanitario general
    ps = models.BooleanField(max_length=100, verbose_name="Parcialmente Seco", null=True, blank=True)
    se = models.BooleanField(verbose_name="Seco", null=True, blank=True)
    sa = models.BooleanField(max_length=100, verbose_name="Sano", null=True, blank=True)
    
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
    causas_int_obra_civil = models.CharField(verbose_name="Causas Int Obra Civil", null=True, blank=True)
    
    
    compensaciones_especiales = models.CharField(verbose_name="Compensaciones Especiales", null=True, blank=True)
    presencia_nidos = models.BooleanField(max_length=100, verbose_name="Presencia de Nidos", null=True, blank=True)
    presencia_epifitas = models.CharField(max_length=100, verbose_name="Presencia de Epifitas", null=True, blank=True)
    brinzales_latizales = models.CharField(max_length=100, verbose_name="Brinzales y Latizales", null=True, blank=True)
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
