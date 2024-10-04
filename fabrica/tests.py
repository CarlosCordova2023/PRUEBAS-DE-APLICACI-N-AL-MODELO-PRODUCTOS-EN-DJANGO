from django.test import TestCase
from django.urls import reverse
from .models import Fabricante

class FabricanteModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Configuración inicial de datos para las pruebas
        Fabricante.objects.create(nombre='Fabrica 1', pais='Ubicación 1')

    def test_model_content_fabricante(self):
        fabricante = Fabricante.objects.get(id=1)
        self.assertEqual(fabricante.nombre, 'Fabrica 1')
        self.assertEqual(fabricante.pais, 'Ubicación 1')
       
























class ProductoTests(TestCase):
    def test_insertar_url_status_code(self):
        response = self.client.get('/fabrica/agregar/')
        self.assertEqual(response.status_code, 200)

    def test_insertar_url_by_name(self):
        url = reverse('agregar_producto')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_insertar_template_used(self):
        url = reverse('agregar_producto')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'fabrica/agregar_producto.html')

    def test_insertar_template_content(self):
        url = reverse('agregar_producto')
        response = self.client.get(url)
        self.assertContains(response, '<title>Agregar Producto</title>')


class ProductoURLTests(TestCase):

    def test_producto_url_status_code(self):
        response = self.client.get('/fabrica/')
        self.assertEqual(response.status_code, 200)


