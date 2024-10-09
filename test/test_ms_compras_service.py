import unittest
from unittest.mock import patch
import requests
from app.services.ms_compras_service import ComprasService
from app.models.compras import Compras

class TestComprasService(unittest.TestCase):

    def setUp(self):
        self.compras_service = ComprasService()
        self.mock_post = patch('app.services.ms_compras_service.requests.post').start()
        self.mock_crear_compra = patch.object(Compras, 'crear_compra').start()

    def tearDown(self):
        patch.stopall()

    @patch('app.services.ms_compras_service.requests.post')
    def test_procesar_pago_y_guardar_compra_exitoso(self, mock_post):
        mock_post.return_value.status_code = 200  # Simula un pago exitoso
        mock_compra = Compras(producto_id=1, direccion_envio="Calle Falsa 123")

        self.mock_crear_compra.return_value = mock_compra
        resultado = self.compras_service.procesar_pago_y_guardar_compra(1, "Calle Falsa 123")

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.producto_id, 1)
        self.assertEqual(resultado.direccion_envio, "Calle Falsa 123")

    @patch('app.services.ms_compras_service.requests.post')
    def test_procesar_pago_y_guardar_compra_fallo_pago(self, mock_post):
        mock_post.return_value.status_code = 400  # Simula un fallo en el pago
        resultado = self.compras_service.procesar_pago_y_guardar_compra(1, "Calle Falsa 123")

        self.assertIsNone(resultado)

    @patch('app.services.ms_compras_service.requests.post')
    def test_procesar_pago_y_guardar_compra_error_conexion(self, mock_post):
        mock_post.side_effect = requests.exceptions.RequestException("Error de conexión")
        resultado = self.compras_service.procesar_pago_y_guardar_compra(1, "Calle Falsa 123")

        self.assertIsNone(resultado)

    @patch.object(Compras, 'crear_compra')
    def test_guardar_compra_exitoso(self, mock_crear_compra):
        mock_compra = Compras(producto_id=1, direccion_envio="Calle Falsa 123")
        mock_crear_compra.return_value = mock_compra

        resultado = self.compras_service.guardar_compra(1, "Calle Falsa 123")

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.producto_id, 1)
        self.assertEqual(resultado.direccion_envio, "Calle Falsa 123")

    def test_guardar_compra_datos_invalidos(self):
        self.mock_crear_compra.side_effect = ValueError("Datos inválidos")
        
        resultado = self.compras_service.guardar_compra(1, "")  # Dirección vacía
        
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()
