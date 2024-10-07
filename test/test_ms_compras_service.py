import unittest
from unittest.mock import patch
from app.services import Compras_service
from app.models import Compras

class TestComprasService(unittest.TestCase):
    compras_serivice=Compras_service()

    @patch('app.services.compras_service.requests.post')
    def test_procesar_pago_y_guardar_compra_exitoso(self, mock_post):

        # Configuración del mock
        mock_post.return_value.status_code = 200
        
        # Suponiendo que el método crear_compra devuelve un objeto de compra
        mock_compra = Compras(producto_id=1, direccion_envio="Calle Falsa 123")
        with patch.object(Compras, 'crear_compra', return_value=mock_compra):
            resultado = self.compras_serivice.procesar_pago_y_guardar_compra(1, "Calle Falsa 123", 100)
        
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.producto_id, 1)
        self.assertEqual(resultado.direccion_envio, "Calle Falsa 123")

    @patch('app.services.compras_service.requests.post')
    def test_procesar_pago_y_guardar_compra_fallo_pago(self, mock_post):
        # Configuración del mock para simular un fallo en el pago
        mock_post.return_value.status_code = 400
        
        resultado = self.compras_serivice.procesar_pago_y_guardar_compra(1, "Calle Falsa 123", 100)
        
        self.assertIsNone(resultado)

    @patch('app.services.compras_service.requests.post')
    def test_procesar_pago_y_guardar_compra_error_conexion(self, mock_post):
        # Configuración del mock para simular un error de conexión
        mock_post.side_effect = Exception("Error de conexión")
        
        resultado = self.compras_serivice.procesar_pago_y_guardar_compra(1, "Calle Falsa 123", 100)
        
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()
