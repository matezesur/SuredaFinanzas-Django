# SuredaFinanzas - Playground Final Project

Proyecto final individual realizado con Python y Django para Coderhouse.

La aplicación es una web estilo blog orientada a educación financiera. Incluye inicio, acerca de mí, listado de páginas, detalle, creación, edición y borrado de publicaciones, autenticación de usuarios, perfiles y mensajería interna.

## Funcionalidades principales

- Home en `/`
- Acerca de mí en `/about/`
- Blog / páginas en `/pages/`
- Detalle de cada page desde el botón **Leer más**
- Mensaje "No hay páginas aún" cuando no existen publicaciones
- Buscador de páginas por título, subtítulo o categoría
- Crear, editar y borrar pages solo con usuario logueado
- Admin de Django con modelos registrados
- Registro de usuarios con username, email y password
- Login y logout
- Perfil con nombre, apellido, email, avatar, biografía, link y fecha de nacimiento
- Edición de perfil y cambio de contraseña
- App de mensajería para enviar y leer mensajes entre usuarios
- Uso de herencia de templates con `base.html`
- Uso de CBV en la app `pages`
- Uso de `LoginRequiredMixin` en vistas basadas en clase
- Uso de decorador `@login_required` en vistas comunes
- Campo de texto enriquecido con CKEditor
- Campo de imagen en pages y avatar de perfil

## Apps del proyecto

- `finanzas`: home y about.
- `pages`: modelo principal del blog.
- `accounts`: registro, login, logout, perfil y edición de usuario.
- `messenger`: mensajes entre usuarios.

## Instalación

1. Clonar el repositorio.
2. Crear entorno virtual:

```bash
python -m venv venv
```

3. Activar entorno virtual:

```bash
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

5. Ejecutar migraciones:

```bash
python manage.py migrate
```

6. Crear superusuario:

```bash
python manage.py createsuperuser
```

7. Levantar el servidor:

```bash
python manage.py runserver
```

8. Entrar en el navegador a:

```bash
http://127.0.0.1:8000/
```

## Importante para la entrega

No se incluye `db.sqlite3` ni la carpeta `media/` en el repositorio. Ambos figuran en `.gitignore`.

Para probar imágenes, cargarlas desde los formularios una vez que el proyecto esté corriendo localmente.
