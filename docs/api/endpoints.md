# API Endpoints

Esta sección documenta los endpoints disponibles en la API del proyecto GAIA AIR Memories.

## Lista de Endpoints

### `GET /api/v1/memories`

- **Descripción**: Obtiene una lista de todas las memorias almacenadas.
- **Parámetros**: 
  - `page` (opcional): Número de página para la paginación.
  - `limit` (opcional): Número de elementos por página.
- **Ejemplo de Solicitud**:
  ```bash
  curl -X GET "https://api.gaia-air-memories.com/api/v1/memories?page=1&limit=10"
  ```
- **Ejemplo de Respuesta**:
  ```json
  {
    "page": 1,
    "limit": 10,
    "total": 100,
    "memories": [
      {
        "id": "1",
        "title": "Memoria 1",
        "description": "Descripción de la memoria 1",
        "created_at": "2023-01-01T00:00:00Z"
      },
      {
        "id": "2",
        "title": "Memoria 2",
        "description": "Descripción de la memoria 2",
        "created_at": "2023-01-02T00:00:00Z"
      }
    ]
  }
  ```

### `POST /api/v1/memories`

- **Descripción**: Crea una nueva memoria.
- **Parámetros**: 
  - `title` (requerido): Título de la memoria.
  - `description` (requerido): Descripción de la memoria.
- **Ejemplo de Solicitud**:
  ```bash
  curl -X POST "https://api.gaia-air-memories.com/api/v1/memories" -H "Content-Type: application/json" -d '{
    "title": "Nueva Memoria",
    "description": "Descripción de la nueva memoria"
  }'
  ```
- **Ejemplo de Respuesta**:
  ```json
  {
    "id": "3",
    "title": "Nueva Memoria",
    "description": "Descripción de la nueva memoria",
    "created_at": "2023-01-03T00:00:00Z"
  }
  ```

### `GET /api/v1/memories/{id}`

- **Descripción**: Obtiene los detalles de una memoria específica.
- **Parámetros**: 
  - `id` (requerido): ID de la memoria.
- **Ejemplo de Solicitud**:
  ```bash
  curl -X GET "https://api.gaia-air-memories.com/api/v1/memories/1"
  ```
- **Ejemplo de Respuesta**:
  ```json
  {
    "id": "1",
    "title": "Memoria 1",
    "description": "Descripción de la memoria 1",
    "created_at": "2023-01-01T00:00:00Z"
  }
  ```

### `PUT /api/v1/memories/{id}`

- **Descripción**: Actualiza los detalles de una memoria específica.
- **Parámetros**: 
  - `id` (requerido): ID de la memoria.
  - `title` (opcional): Nuevo título de la memoria.
  - `description` (opcional): Nueva descripción de la memoria.
- **Ejemplo de Solicitud**:
  ```bash
  curl -X PUT "https://api.gaia-air-memories.com/api/v1/memories/1" -H "Content-Type: application/json" -d '{
    "title": "Memoria Actualizada",
    "description": "Descripción actualizada de la memoria"
  }'
  ```
- **Ejemplo de Respuesta**:
  ```json
  {
    "id": "1",
    "title": "Memoria Actualizada",
    "description": "Descripción actualizada de la memoria",
    "created_at": "2023-01-01T00:00:00Z"
  }
  ```

### `DELETE /api/v1/memories/{id}`

- **Descripción**: Elimina una memoria específica.
- **Parámetros**: 
  - `id` (requerido): ID de la memoria.
- **Ejemplo de Solicitud**:
  ```bash
  curl -X DELETE "https://api.gaia-air-memories.com/api/v1/memories/1"
  ```
- **Ejemplo de Respuesta**:
  ```json
  {
    "message": "Memoria eliminada exitosamente"
  }
  ```

## Notas

- Asegúrese de manejar adecuadamente los errores y las respuestas de la API.
- Utilice autenticación y autorización según sea necesario para proteger los endpoints.
