from app.models.compras import Compras
import requests
import logging

class ComprasService:
    URL_PAGO = "http://localhost:5001/procesar_pago"
    URL_STOCK = "http://localhost:5002/stock"

    @staticmethod
    def procesar_pago_y_guardar_compra(producto_id, direccion_envio):
        datos_pago = {
            "producto_id": producto_id,
            "direccion_envio": direccion_envio,
        }
        try:
            respuesta = requests.post(ComprasService.URL_PAGO, json=datos_pago)
            if respuesta.status_code == 200:
                compra = Compras.crear_compra(producto_id, direccion_envio)
                datos_stock = {
                    "producto_id": producto_id,
                    "cantidad": 1
                }
                respuesta_stock = requests.post(ComprasService.URL_STOCK, json=datos_stock)
                if respuesta_stock.status_code == 200:
                    logging.info("Stock actualizado exitosamente.")
                else:
                    logging.error("Error al actualizar el stock: %s", respuesta_stock.json())
                return compra
            else:
                logging.error("Error al procesar el pago: %s", respuesta.json())
                return None
        except requests.exceptions.RequestException as e:
            logging.error("Error al conectar con el microservicio de pagos: %s", str(e))
            return None

    def guardar_compra(self, producto_id, direccion_envio):
        try:
            return Compras.crear_compra(producto_id, direccion_envio)
        except Exception as e:
            logging.error("Error al guardar la compra: %s", str(e))
            return None
