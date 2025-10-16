# 🐾 Pet Care API

## 📝 Descripción del Proyecto

**Pet Care API** es una API REST desarrollada con Django y Django REST Framework que permite gestionar información de mascotas y sus dueños. El sistema permite realizar operaciones CRUD completas sobre ambas entidades, además de implementar funcionalidades de búsqueda y filtrado.

---

## 📦 Instalación y Configuración

### Pasos de Instalación

1. **Clonar el repositorio**
    ```bash
    git clone https://github.com/josep-rivera/dae-evaluacion-2.git
    ```

2. **Crear y activar entorno virtual**

    En Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    En Linux/Mac:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Instalar dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4. **Realizar migraciones**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

---

## 🚀 Ejecutar el Servidor

Para iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://localhost:8000`

---

## 📡 Endpoints Disponibles

### Base URL
```
http://localhost:8000/api/
```

---

### 🐶 Mascotas (Entidad 1)

#### 1. Listar todas las mascotas

**Endpoint:**
```
GET /api/entidad1/
```

**Postman:**
- Method: `GET`
- URL: `http://localhost:8000/api/entidad1/`

**Respuesta exitosa (200 OK):**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "nombre": "Max",
            "especie": "Perro",
            "edad": 3,
            "dueño": 1
        },
        {
            "id": 2,
            "nombre": "Luna",
            "especie": "Gato",
            "edad": 2,
            "dueño": 2
        }
    ]
}
```

---

#### 2. Crear una nueva mascota

**Endpoint:**
```
POST /api/entidad1/
```

**Postman:**
- Method: `POST`
- URL: `http://localhost:8000/api/entidad1/`
- Headers: 
  - `Content-Type: application/json`
- Body (raw - JSON):
```json
{
    "nombre": "Rocky",
    "especie": "Perro",
    "edad": 5,
    "dueño": 1
}
```

**Respuesta exitosa (201 Created):**
```json
{
    "id": 3,
    "nombre": "Rocky",
    "especie": "Perro",
    "edad": 5,
    "dueño": 1
}
```

---

#### 3. Ver detalle de una mascota (con información del dueño)

**Endpoint:**
```
GET /api/entidad1/{id}/
```

**Postman:**
- Method: `GET`
- URL: `http://localhost:8000/api/entidad1/1/`

**Respuesta exitosa (200 OK):**
```json
{
    "id": 1,
    "nombre": "Max",
    "especie": "Perro",
    "edad": 3,
    "dueño": {
        "id": 1,
        "nombre": "Juan Pérez",
        "telefono": "987654321"
    },
    "dueño_nombre": "Juan Pérez"
}
```

---

#### 4. Actualizar una mascota (PUT - actualización completa)

**Endpoint:**
```
PUT /api/entidad1/{id}/
```

**Postman:**
- Method: `PUT`
- URL: `http://localhost:8000/api/entidad1/1/`
- Headers: 
  - `Content-Type: application/json`
- Body (raw - JSON):
```json
{
    "nombre": "Max Actualizado",
    "especie": "Perro",
    "edad": 4,
    "dueño": 1
}
```

**Respuesta exitosa (200 OK):**
```json
{
    "id": 1,
    "nombre": "Max Actualizado",
    "especie": "Perro",
    "edad": 4,
    "dueño": 1
}
```

---

#### 5. Actualizar parcialmente una mascota (PATCH)

**Endpoint:**
```
PATCH /api/entidad1/{id}/
```

**Postman:**
- Method: `PATCH`
- URL: `http://localhost:8000/api/entidad1/1/`
- Headers: 
  - `Content-Type: application/json`
- Body (raw - JSON):
```json
{
    "edad": 5
}
```

**Respuesta exitosa (200 OK):**
```json
{
    "id": 1,
    "nombre": "Max Actualizado",
    "especie": "Perro",
    "edad": 5,
    "dueño": 1
}
```

---

#### 6. Eliminar una mascota

**Endpoint:**
```
DELETE /api/entidad1/{id}/
```

**Postman:**
- Method: `DELETE`
- URL: `http://localhost:8000/api/entidad1/3/`

**Respuesta exitosa (204 No Content)**

---

#### 7. Buscar mascotas (por nombre o especie)

**Endpoint:**
```
GET /api/entidad1/?search={término}
```

**Postman - Buscar por nombre:**
- Method: `GET`
- URL: `http://localhost:8000/api/entidad1/?search=Max`

**Postman - Buscar por especie:**
- Method: `GET`
- URL: `http://localhost:8000/api/entidad1/?search=Perro`

**Respuesta exitosa (200 OK):**
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "nombre": "Max",
            "especie": "Perro",
            "edad": 3,
            "dueño": 1
        }
    ]
}
```

---

#### 8. Filtrar mascotas por especie

**Endpoint:**
```
GET /api/entidad1/?especie={especie}
```

**Postman:**
- Method: `GET`
- URL: `http://localhost:8000/api/entidad1/?especie=Perro`

**Respuesta exitosa (200 OK):**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "nombre": "Max",
            "especie": "Perro",
            "edad": 3,
            "dueño": 1
        },
        {
            "id": 3,
            "nombre": "Rocky",
            "especie": "Perro",
            "edad": 5,
            "dueño": 1
        }
    ]
}
```

---

#### 9. Filtrar mascotas por edad

**Endpoint:**
```
GET /api/entidad1/?edad={edad}
```

**Postman:**
- Method: `GET`
- URL: `http://localhost:8000/api/entidad1/?edad=3`

**Respuesta exitosa (200 OK):**
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "nombre": "Max",
            "especie": "Perro",
            "edad": 3,
            "dueño": 1
        }
    ]
}
```

---

### 👤 Dueños (Entidad 2)

#### 1. Listar todos los dueños

**Endpoint:**
```
GET /api/entidad2/
```

**Postman:**
- Method: `GET`
- URL: `http://localhost:8000/api/entidad2/`

**Respuesta exitosa (200 OK):**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "nombre": "Juan Pérez",
            "telefono": "987654321"
        },
        {
            "id": 2,
            "nombre": "María García",
            "telefono": "912345678"
        }
    ]
}
```

---

#### 2. Crear un nuevo dueño

**Endpoint:**
```
POST /api/entidad2/
```

**Postman:**
- Method: `POST`
- URL: `http://localhost:8000/api/entidad2/`
- Headers: 
  - `Content-Type: application/json`
- Body (raw - JSON):
```json
{
    "nombre": "Carlos López",
    "telefono": "999888777"
}
```

**Respuesta exitosa (201 Created):**
```json
{
    "id": 3,
    "nombre": "Carlos López",
    "telefono": "999888777"
}
```

---

#### 3. Ver detalle de un dueño

**Endpoint:**
```
GET /api/entidad2/{id}/
```

**Postman:**
- Method: `GET`
- URL: `http://localhost:8000/api/entidad2/1/`

**Respuesta exitosa (200 OK):**
```json
{
    "id": 1,
    "nombre": "Juan Pérez",
    "telefono": "987654321"
}
```

---

#### 4. Actualizar un dueño (PUT)

**Endpoint:**
```
PUT /api/entidad2/{id}/
```

**Postman:**
- Method: `PUT`
- URL: `http://localhost:8000/api/entidad2/1/`
- Headers: 
  - `Content-Type: application/json`
- Body (raw - JSON):
```json
{
    "nombre": "Juan Pérez Actualizado",
    "telefono": "987654999"
}
```

**Respuesta exitosa (200 OK):**
```json
{
    "id": 1,
    "nombre": "Juan Pérez Actualizado",
    "telefono": "987654999"
}
```

---

#### 5. Actualizar parcialmente un dueño (PATCH)

**Endpoint:**
```
PATCH /api/entidad2/{id}/
```

**Postman:**
- Method: `PATCH`
- URL: `http://localhost:8000/api/entidad2/1/`
- Headers: 
  - `Content-Type: application/json`
- Body (raw - JSON):
```json
{
    "telefono": "987654000"
}
```

**Respuesta exitosa (200 OK):**
```json
{
    "id": 1,
    "nombre": "Juan Pérez Actualizado",
    "telefono": "987654000"
}
```

---

#### 6. Eliminar un dueño

**Endpoint:**
```
DELETE /api/entidad2/{id}/
```

**Postman:**
- Method: `DELETE`
- URL: `http://localhost:8000/api/entidad2/3/`

**Respuesta exitosa (204 No Content)**

---

## 📸 Capturas de Pantalla

**Listado de Mascotas:**
```
http://localhost:8000/api/entidad1/
```

**Detalle de Mascota con Dueño:**
```
http://localhost:8000/api/entidad1/1/
```
---

## 👨‍💻 Autor

Rivera Munarez, Josep Danton

---