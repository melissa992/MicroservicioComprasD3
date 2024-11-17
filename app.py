from app import create_app
from app.routes.compras_route import compras_bp
from flasgger import Swagger  # Importa Swagger

app = create_app()

# Configura Swagger
swagger = Swagger(app)

app.app_context().push()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
