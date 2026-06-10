# 🚀 Aprendizaje de Python y Flask

Este repositorio contiene las actividades realizadas durante el aprendizaje de Python, Flask y manejo de bases de datos con SQLAlchemy.

---

## 📌 Actividad 12: API REST con Flask + SQLAlchemy (CRUD Películas)

En la carpeta `12-Api-Rest-Flask` se desarrolla una API REST para la gestión de películas usando Flask y SQLAlchemy.

Se trabaja:

- Creación de API REST con Flask
- Modelo de datos con SQLAlchemy
- Base de datos SQLite
- CRUD completo:
  - Crear (POST)
  - Leer (GET)
  - Actualizar (PUT)
  - Eliminar (DELETE)
- Manejo de datos en formato JSON
- Rutas dinámicas con Flask
- Serialización con `to_dict()`

💡 Permite construir una API funcional con operaciones básicas sobre una base de datos.

---

## 📌 Actividad 10: Aplicación Modular con Flask (App Factory + Blueprints + Migrate)

En la carpeta `10-App-Factory-Migrate-Flask` se desarrolla una aplicación web estructurada con Flask utilizando el patrón App Factory, Blueprints y Flask-Migrate para el manejo de base de datos.

Se trabaja:

- Estructura modular con patrón App Factory
- Organización del proyecto en `src/` con módulos independientes
- Uso de Blueprints para separar funcionalidades (`core`, `miembros`, `tareas`)
- Implementación de CRUD completo para miembros y tareas
- Uso de SQLAlchemy como ORM
- Migraciones de base de datos con Flask-Migrate y Alembic
- Uso de SQLite como base de datos local
- Separación de modelos, rutas y templates por módulo
- Uso de Jinja2 para renderizado de vistas

💡 Esta actividad permite aplicar una arquitectura escalable y profesional en una aplicación Flask organizada por módulos.

---

## 📌 Actividad 7: Modelado de Base de Datos con SQLAlchemy

En la carpeta `07-Modelo_DB_SQLAlchemy` se desarrolla un sistema de gestión de biblioteca digital utilizando Flask y SQLAlchemy ORM.

Se trabaja:

- Definición de modelos con SQLAlchemy
- Relaciones 1–N entre Autor y Libro
- Relaciones N–M entre Libro y Género
- Uso de tabla intermedia `libro_genero`
- Inicialización de la base de datos
- Inserción de datos relacionados
- Consulta de datos con ORM
- Actualización de registros
- Eliminación en cascada usando `cascade="all, delete-orphan"`

💡 Esta actividad permite comprender el modelado de bases de datos relacionales utilizando ORM en Flask.

---

## 📌 Actividad 6: CRUD con ORM (Video Flask + SQLAlchemy)

En la carpeta `06-CRUD_ORM_Flask` se desarrolla un sistema CRUD utilizando Flask junto con SQLAlchemy como ORM.

Se trabaja:

- Definición de modelos con SQLAlchemy
- Uso de `db.Model` para mapear tablas
- Crear registros (Create)
- Leer registros (Read)
- Actualizar registros (Update)
- Eliminar registros (Delete)
- Uso de `session.commit()`

💡 Esta actividad permite trabajar con bases de datos sin escribir SQL directamente.

---

## 📌 Actividad 5: CRUD completo con Flask + SQLite

En la carpeta `05-CRUD_BD_Flask` se desarrolla una aplicación web con Flask conectada a SQLite implementando un CRUD completo.

Se trabaja:

- Crear registros (Create)
- Leer registros (Read)
- Actualizar registros (Update)
- Eliminar registros (Delete)
- Uso de rutas dinámicas en Flask
- Manejo de formularios con `request.form`
- Conexión y manipulación de base de datos SQLite

💡 Esta actividad integra todo lo aprendido en un sistema funcional de gestión de contactos.

---

## 📌 Actividad 4: Conexión a Base de Datos con SQLite

En la carpeta `04-Conexion_BD` se trabaja con una base de datos SQLite usando Python.

Se realiza:

- Conexión a la base de datos con `sqlite3`
- Creación de tablas (cursos, estudiantes, inscripciones)
- Inserción de datos
- Consultas con SELECT

💡 Esta actividad permite entender cómo manejar bases de datos desde Python.

---

## 📌 Actividad 3: Sistema de Login con Flask

En la carpeta `03-Gestion Paginas` se desarrolla un login básico utilizando Flask.

Se trabaja:

- Formulario de inicio de sesión
- Validación de usuario
- Redirección entre páginas
- Uso de plantillas HTML (Jinja2)
- Archivos estáticos (CSS y Bootstrap)

💡 Esta actividad simula un sistema de autenticación sencillo en una aplicación web.

---

## 📌 Actividad 2: Gestión de Rutas con Flask (Video 2)

En la carpeta `02-Gestion_Rutas_Flask` se implementan ejemplos rutas usando Flask.

Se trabajan:

- Rutas básicas
- Rutas con parámetros
- Rutas con tipos de datos
- CRUD básico con API

💡 Esta actividad se enfoca en el manejo de rutas en aplicaciones web con Flask.

---

## 📌 Actividad 1: Desarrollo de Python Esencial (Video 1)

En el archivo `app.py` se desarrollan ejemplos básicos de Python.

Se practican:

- Variables, operadores y datos
- Condicionales y bucles
- Listas, diccionarios y funciones

💡 Esta actividad sirve como introducción a los conceptos fundamentales de Python.

---

## 🛠️ Tecnologías utilizadas

- Python 🐍
- Flask 🌐
- SQLAlchemy 🧱
- SQLite 🗄️
- HTML + CSS 🎨
- Bootstrap 💻