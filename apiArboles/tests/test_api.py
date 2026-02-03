from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Arbol, Taxonomia
import os
from django.conf import settings

class ArbolTests(APITestCase):
    def setUp(self):
        # Create initial Taxonomia
        self.taxonomia = Taxonomia.objects.create(
            codigo="TX001",
            nombre_comun="Roble",
            nombre_cientifico="Quercus humboldtii"
        )
        self.arbol_url = '/api/arboles/'

    def test_create_and_retrieve_arbol(self):
        """
        Ensure we can create a new Arbol object with photo and retrieve it.
        """
        # Path to a real photo from assets
        photo_path = os.path.join(settings.BASE_DIR, 'assets', 'registro_fotografico', '1- (1).jpg')
        
        # Verify file exists
        if not os.path.exists(photo_path):
            self.skipTest(f"Test photo not found at {photo_path}")

        with open(photo_path, 'rb') as photo:
            data = {
                'no_arbol': '1',
                'codigo_distrital': '',
                'taxonomia_id': self.taxonomia.id,
                'pap_m': 1.5,
                'alt_tot_m': 10.5,
                # 'uploaded_fotos': photo # This needs to be handled carefully in list
                'uploaded_fotos': [photo] 
            }
            
            # Since we are uploading files, format needs to be multipart
            response = self.client.post(self.arbol_url, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Arbol.objects.count(), 1)
        
        arbol = Arbol.objects.get()
        self.assertEqual(arbol.no_arbol, '1')
        self.assertEqual(arbol.taxonomia, self.taxonomia)
        
        # Check if photos were created
        self.assertTrue(arbol.fotos.count() > 0)
        
        # Check if lat/long were extracted (assuming the test photo has EXIF)
        # We print it to see the result, as we don't know for sure if the specific asset has gps
        print(f"Extracted Lat: {arbol.latitud}, Lon: {arbol.longitud}, Date: {arbol.fecha_visita}")

        # Now test Retrieval (GET)
        response_get = self.client.get(f"{self.arbol_url}{arbol.id}/")
        
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        
        response_data = response_get.json()
        
        # Check basic fields
        self.assertEqual(response_data['no_arbol'], '1')
        
        # Check Taxonomia Detail
        self.assertIsNotNone(response_data.get('taxonomia_detalle'))
        self.assertEqual(response_data['taxonomia_detalle']['codigo'], 'TX001')
        
        # Check Photos in response
        self.assertTrue(len(response_data['fotos']) > 0)
        self.assertIn('imagen', response_data['fotos'][0])

    def test_create_arbol_all_booleans(self):
        """
        Test creating an Arbol with all BooleanField set to True and verifying geolocation from photo.
        """
        photo_path = os.path.join(settings.BASE_DIR, 'assets', 'registro_fotografico', '1- (1).jpg')
        if not os.path.exists(photo_path):
            self.skipTest(f"Test photo not found at {photo_path}")

        boolean_fields = [
            'er', 'paa', 'pat', 'rs', 'rb', 'ca', 'rp', 'rpc', 'ddr', 'des', 'no',
            'b', 'bb', 'b_basales', 'horquilla_v', 'horquilla_u', 'to', 'fr', 'i', 'gdi', 'mi', 
            'c', 'rv', 'ac', 'an_interv', 'dc', 'sb', 'ag_interv', 'po', 'pe', 
            'dm_l', 'dm_g', 'dm_m', 'gri', 'fis', 'cav', 'ap', 'ci',
            'he_c', 'an_c', 'ag_c', 'ne_c', 'tu_c', 'cl_c', 'ma_c', 'ca_c', 'pl_c', 'mi_c', 
            'c_c', 'ro_c', 'psu_c', 'pt_c', 'pla_c', 'pi_c', 'na_c',
            're_f', 'hg_f', 'ch_f', 'pl_f', 'go_f', 'tu_f', 'ag_f', 'pi_f', 'na_f',
            'pl_r', 'na_r',
            'ps', 'se', 'sa',
            'zp', 'ma_other', 'iiv', 'ie', 'imu', 'ira', 'ire', 'hx', 'pv', 'esv', 'auai', 
            'id_indicador', 'des_indicador', 'di', 'def_field', 'eie', 'ni',
            'presencia_nidos', 
            'ta_tec', 'co_tec', 'tra_tec', 'pre_tec', 'pca_tec', 'pac_tec', 'pe_tec', 
            'es_tec', 'sa_tec', 'pr_tec', 'te_tec', 'ti_tec'
        ]
        
        with open(photo_path, 'rb') as photo:
            data = {
                'no_arbol': '2',
                'codigo_distrital': 'BOOL_TEST',
                'taxonomia_id': self.taxonomia.id,
                'uploaded_fotos': [photo]
            }
            
            # Set all booleans to True
            for field in boolean_fields:
                data[field] = True
            
            response = self.client.post(self.arbol_url, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        arbol_id = response.data['id']
        arbol = Arbol.objects.get(id=arbol_id)
        
        # Verify GPS Extraction
        self.assertIsNotNone(arbol.latitud)
        self.assertIsNotNone(arbol.longitud)

        # Verify they are all True
        for field in boolean_fields:
            self.assertTrue(getattr(arbol, field), f"Field {field} should be True")
            
    def test_patch_and_get_arbol(self):
        """
        Test creating with photo (to get coords) then updating CharFields via PATCH and verifying with GET.
        """
        photo_path = os.path.join(settings.BASE_DIR, 'assets', 'registro_fotografico', '1- (1).jpg')
        if not os.path.exists(photo_path):
            self.skipTest(f"Test photo not found at {photo_path}")

        # 1. Create initial arbol via API to trigger EXIF extraction
        with open(photo_path, 'rb') as photo:
            create_data = {
                'no_arbol': '3',
                'codigo_distrital': 'PATCH_TEST',
                'taxonomia_id': self.taxonomia.id,
                'barrio': 'Barrio Original',
                'localidad': 'Localidad Original',
                'uploaded_fotos': [photo]
            }
            response_create = self.client.post(self.arbol_url, create_data, format='multipart')
        
        self.assertEqual(response_create.status_code, status.HTTP_201_CREATED)
        arbol_id = response_create.data['id']
        
        # Verify Coords exists before PATCH
        arbol_before = Arbol.objects.get(id=arbol_id)
        self.assertIsNotNone(arbol_before.latitud)
        print(f"\n[PATCH Test] Original Lat: {arbol_before.latitud}")
        
        patch_url = f"{self.arbol_url}{arbol_id}/"
        
        # 2. PATCH data
        patch_data = {
            'barrio': 'Barrio Nuevo',
            'localidad': 'Localidad Nueva',
            'conclusion_concepto_tecnico': 'Concepto actualizado via PATCH'
        }
        
        response_patch = self.client.patch(patch_url, patch_data)
        self.assertEqual(response_patch.status_code, status.HTTP_200_OK)
        
        # Verify response matches patch
        self.assertEqual(response_patch.data['barrio'], 'Barrio Nuevo')
        self.assertEqual(response_patch.data['localidad'], 'Localidad Nueva')
        
        # 3. GET data to ensure persistence
        response_get = self.client.get(patch_url)
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        
        data = response_get.data
        self.assertEqual(data['barrio'], 'Barrio Nuevo')
        self.assertEqual(data['conclusion_concepto_tecnico'], 'Concepto actualizado via PATCH')