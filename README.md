# **MS Compras - Microservicio de Gestión de Compras**

Este repositorio contiene el código fuente del microservicio de compras desarrollado en Python utilizando el framework Flask, con integración a una base de datos PostgreSQL. El proyecto forma parte de un sistema más grande para la gestión de compras y ventas, desarrollado como parte de la materia **Desarrollo de Software** en **3° Año de Ingeniería en Sistemas UTN-FRSR**.

## **Requisitos Previos**

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias y tecnologías:

- **Docker** y **Docker Compose**
- **Python 3.12**
- **PostgreSQL 17**
- **Flask 3.0.3**
- **Flask-SQLAlchemy 3.0.5**
- **Flask-Migrate 4.0.4**
- **pytest** para pruebas
- **psycopg2-binary 2.9.7**

## **Instalación y Configuración**

### 1. **Clonar el Repositorio**

```bash
git https://github.com/melissa992/MicroservicioComprasD3
cd ms-compras
```

### 2. **Crear un Entorno Virtual y Activarlo**

Es recomendable usar un entorno virtual para manejar las dependencias del proyecto:

```bash
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
```

### 3. **Instalar Dependencias**

```bash
pip install -r requirements.txt
```

### 4. **Configurar las Variables de Entorno**

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_RECORD_QUERIES = True
DATABASE_URL=postgresql://usuario:contrasena@localhost:5433/bdcompras
FLASK_CONTEXT = 'development'
```

### 5. **Iniciar los Contenedores Docker**

Asegúrate de tener **Docker** instalado, ingresa a la carpeta de docker.
``` bash
cd ./docker
```

Luego, ejecuta los contenedores de base de datos con:

```bash
docker-compose up -d
```

Esto levantará un contenedor con PostgreSQL en el puerto `5433`.

## **Estructura del Proyecto**

```
ms-compras/
│
├── app/                   # Código fuente del microservicio
│   ├── models/            # Modelos de base de datos
│   ├── routes/            # Rutas o endpoints
│   ├── templates/         # Plantillas HTML
│   └── __init__.py        # Configuración del microservicio
│
├── migrations/            # Migraciones de la base de datos
├── tests/                 # Pruebas unitarias con pytest
├── .env                   # Variables de entorno (no se sube al repo)
├── Dockerfile             # Definición de la imagen Docker
├── docker-compose.yml     # Configuración Docker Compose
├── requirements.txt       # Lista de dependencias
├── README.md              # Documentación del proyecto
└── run.py                 # Punto de entrada de la aplicación
```

## **Pruebas**

Para ejecutar las pruebas unitarias, usa `unittes`:

```bash
python -m test.test_name.py
```

## **Docker**

Este proyecto está configurado para ejecutarse en contenedores Docker. Si deseas construir la imagen manualmente:

```bash
docker build -t ms-compras .
```

## **Tecnologías Utilizadas**

- **Flask** - Framework de desarrollo web
- **SQLAlchemy** - ORM para la gestión de la base de datos
- **PostgreSQL** - Base de datos relacional
- **Docker** - Para la contenedorización del servicio
- **pytest** - Framework para pruebas unitarias

