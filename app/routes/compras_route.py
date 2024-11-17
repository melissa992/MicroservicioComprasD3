from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.models.compras import Compras
from app import db
from datetime import datetime

compras_bp = Blueprint("compras", __name__)

@compras_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Compras'],
    'description': 'Crear una nueva compra',
    'parameters': [
        {
            'name': 'producto_id',
            'in': 'json',
            'type': 'integer',
            'required': True,
            'description': 'ID del producto a comprar'
        },
        {
            'name': 'direccion_envio',
            'in': 'json',
            'type': 'string',
            'required': True,
            'description': 'Dirección de envío de la compra'
        }
    ],
    'responses': {
        '201': {
            'description': 'Compra creada exitosamente',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'producto_id': {'type': 'integer'},
                    'direccion_envio': {'type': 'string'}
                }
            }
        },
        '400': {
            'description': 'Datos inválidos'
        },
        '500': {
            'description': 'Error al procesar la compra'
        }
    }
})
def create_compra():
    data = request.get_json()

    if not data or not "producto_id" in data or not "direccion_envio" in data:
        return jsonify({"error": "Datos inválidos"}), 400

    compra = Compras.crear_compra(data["producto_id"], data["direccion_envio"])

    if compra is None:
        return jsonify({"error": "Error al procesar la compra"}), 500

    return (
        jsonify(
            {
                "id": compra.id,
                "producto_id": compra.producto_id,
                "direccion_envio": compra.direccion_envio,
            }
        ),
        201,
    )


@compras_bp.route("/<int:id>", methods=["GET"])
@swag_from({
    'tags': ['Compras'],
    'description': 'Obtener una compra por ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la compra a obtener'
        }
    ],
    'responses': {
        '200': {
            'description': 'Compra encontrada',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'producto_id': {'type': 'integer'},
                    'direccion_envio': {'type': 'string'}
                }
            }
        },
        '404': {
            'description': 'Compra no encontrada'
        }
    }
})
def get_compra(id):
    compra = Compras.obtener_compra_por_id(id)
    if compra is None:
        return jsonify({"error": "Compra no encontrada"}), 404
    return jsonify(
        {
            "id": compra.id,
            "producto_id": compra.producto_id,
            "direccion_envio": compra.direccion_envio,
        }
    )


@compras_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['Compras'],
    'description': 'Obtener todas las compras',
    'responses': {
        '200': {
            'description': 'Lista de compras',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'producto_id': {'type': 'integer'},
                        'direccion_envio': {'type': 'string'}
                    }
                }
            }
        }
    }
})
def get_compras():
    compras = Compras.obtener_compras()
    return jsonify(
        [
            {
                "id": compra.id,
                "producto_id": compra.producto_id,
                "direccion_envio": compra.direccion_envio,
            }
            for compra in compras
        ]
    )


@compras_bp.route("/<int:id>", methods=["PUT"])
@swag_from({
    'tags': ['Compras'],
    'description': 'Actualizar los detalles de una compra',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la compra a actualizar'
        },
        {
            'name': 'producto_id',
            'in': 'json',
            'type': 'integer',
            'required': False,
            'description': 'Nuevo ID del producto'
        },
        {
            'name': 'direccion_envio',
            'in': 'json',
            'type': 'string',
            'required': False,
            'description': 'Nueva dirección de envío'
        }
    ],
    'responses': {
        '200': {
            'description': 'Compra actualizada exitosamente',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'producto_id': {'type': 'integer'},
                    'direccion_envio': {'type': 'string'}
                }
            }
        },
        '404': {
            'description': 'Compra no encontrada'
        }
    }
})
def update_compra(id):
    compra = Compras.obtener_compra_por_id(id)
    if compra is None:
        return jsonify({"error": "Compra no encontrada"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    compra.producto_id = data.get("producto_id", compra.producto_id)
    compra.direccion_envio = data.get("direccion_envio", compra.direccion_envio)
    db.session.commit()

    return jsonify(
        {
            "id": compra.id,
            "producto_id": compra.producto_id,
            "direccion_envio": compra.direccion_envio,
        }
    )


@compras_bp.route("/<int:id>", methods=["DELETE"])
@swag_from({
    'tags': ['Compras'],
    'description': 'Eliminar una compra por ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la compra a eliminar'
        }
    ],
    'responses': {
        '200': {
            'description': 'Compra eliminada exitosamente'
        },
        '404': {
            'description': 'Compra no encontrada'
        }
    }
})
def delete_compra(id):
    compra = Compras.obtener_compra_por_id(id)
    if compra is None:
        return jsonify({"error": "Compra no encontrada"}), 404

    db.session.delete(compra)
    db.session.commit()
    return jsonify({"message": "Compra eliminada"}), 200
