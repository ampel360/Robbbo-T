
# 📡 Routers - CMS-KIT Backend (FastAPI)

Este módulo contiene los **routers de la API REST** para el sistema de gestión de contenidos (CMS-KIT) del proyecto COAFI.

Los routers encapsulan la lógica de enrutamiento para los diferentes recursos del backend, siguiendo el principio de **modularidad** y permitiendo una integración limpia con sistemas federados o descentralizados, como nodos GAIA-AIR o identidades distribuidas basadas en `gaia-token`.

---

## 📁 Estructura actual

```
routers/
└── users.py
```

---

## 🔐 `users.py` – Gestión de Identidades

Este router implementa una interfaz REST para el manejo de usuarios, compatible con:

- **OAuth2 / JWT**
- **Tokens descentralizados** (futuramente interoperable con `gaia-token`)
- **Autenticación federada** (pensado para integrarse con nodos distribuidos)

### Endpoints disponibles

| Método | Ruta              | Descripción                                  | Seguridad     |
|--------|-------------------|----------------------------------------------|----------------|
| POST   | `/users/`         | Crear un nuevo usuario                       | Público        |
| GET    | `/users/`         | Listar usuarios con paginación               | Requiere token |
| GET    | `/users/me`       | Obtener el usuario autenticado actual        | Requiere token |
| GET    | `/users/{id}`     | Obtener un usuario por ID                    | Requiere token |
| DELETE | `/users/{id}`     | Eliminar un usuario                          | Requiere token |

### Dependencias utilizadas

- `get_db`: Inyección de sesión de base de datos (SQLAlchemy)
- `get_current_active_user`: Middleware de autenticación (JWT / OAuth2)

---

## 🎯 Objetivo

Desacoplar y escalar funcionalidades del backend para permitir:

- **Orquestación modular**
- **Federación de identidades**
- **Auditoría distribuida**
- **Autenticación unificada (SSO-ready)**

---

## 🚧 Roadmap (pendiente)

- [ ] Integración con `gaia-token` como identidad base descentralizada.
- [ ] Enlace con servicios de verificación externa (SSI, DID).
- [ ] Soporte para roles y permisos granularizados.
- [ ] Firma de tokens asimétricos (ECDSA).

---

## 📎 Requisitos

- Python 3.10+
- FastAPI
- SQLAlchemy
- Authlib / PyJWT
- Base de datos compatible (PostgreSQL, SQLite para desarrollo)

---

## 🤖 Autoría

Parte del backend de `CMS-KIT`, dentro de la arquitectura distribuida de **COAFI** (Content Management System as Container and Orchestrator for Aerospace Fixed Index).

Diseñado para integrarse con sistemas federados en **entornos aeroespaciales éticos y cuánticos**.

---

