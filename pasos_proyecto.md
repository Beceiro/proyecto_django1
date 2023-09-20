# Proyecto Django - Práctica

## Pasos realizados

1. Instalar django usando el comando

    ```bash
    pip install django
    ```

2. Crear proyecto

    ```bash
    python -m django startproject proyecto_django1
    ```

3. Crear aplicación

   ```bash
    cd proyecto_django1

    python manage.py startapp app_django2
    ```

4. Aplicar migraciones de ***app_django2*** con ``$ python manage.py migrate``
5. Primer lanzamiento servidor ``python manage.py runserver`` - Muestra el link para acceder a la pagina
6. Agregar aplicación a la lista de apps en el archivo **settings.py** - ``INSTALLED_APPS = []``
7. Modifica el archivo **models.py** de la aplicación

    ```py
        # Modelo de base de datos para clientes
        # Se aplican los atributos customer, party_id, name, email (4)

        class Customer(models.Model):
            customer = models.CharField(("Clientes"), max_length=50)
            party_id = models.IntegerField()
            name = models.CharField(max_length=50)
            email = models.EmailField()
    ```

8. ``$ python manage.py makemigrations`` para subir los cambios seguido de ``$ python manage.py migrate`` para aplicarlos
9. La acción anterior crea una base de datos ***db.sqlite3*** que contiene la información volcada en el archivo ***models.py***

## Pasos a realizar

1) - [x] Verificar que el comando ``$ python manage.py runserver`` funcione correctamente
2) - [ ] Crear carpeta templates/ para empezar a agregarlos.
    > *La carpeta templates se crea dentro de la carpeta del proyecto y lleva dentro un archivo HTML-Django (Distinto a HTML5).*
3) - [ ] Entender el uso de HttpResponse y en que archivos se escribe
4) - [ ] Repasar modelos de django

## Entorno virtual

El entorno virtual (VENV) nos permite trabajar con diferentes recursos que necesite el proyecto en python y que quede guardado en una carpeta **virtual**

Si no trabajamos en un entorno virtual todo el trabajo queda asentado de manera local y es más engorroso de limpiar en caso de que se lo desee.

```bash
python -m venv virt_env
```

---------

## Comandos terminal django

```bash
pip freeze > requirements.txt
python manage.py runserver 4000
git clone
git push
```

## Notas clase 19/9

Archivo **views.py** se crean dentro de las carpetas de las aplicaciones.

Se crea una carpeta templates/ dentro de la carpeta de la ***aplicacion***.
Cuando Django hace el runserver se mezclan todas carpetas y archivos que tengan el mismo nombre.

Para prevenir esto, dentro de la carpeta de la aplicacion se crea una carpeta con el mismo nombre de la aplicacion

```py
# Dentro del archivo views.py
from django.template import Template, Conext
from django.http import HttpResponse

def inicio(request):
    archivo = open('Se copia el relative path del archivo HTML','r')
    template = Template(archivo.read())
    archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

#v2 - Se agrega 'Loader' al import y se modifica variable 'template'
from django.template import Template, Conext, Loader
from django.http import HttpResponse

def inicio(request):

    diccionario = {
        'fecha': datetime.now()
    }

    template = loader.get_template(r'Ruta del archivo HTML')
    template_renderizado = template.render(diccionario)
    return HttpResponse(template_renderizado)

#v3 - Agregando 'render' desde django.shortcuts resumimos todo dentro del return de la funcion
from django.template import Template, Conext, Loader
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime.now

def inicio(request):
    diccionario = {
        'fecha': datetime.now()
    }

    return render(request, r'Ruta de archivo HTML', datos)
```

Se recomienda crear un archivo URL por cada aplicacion >> Dentro de la carpeta de la aplicacion se crea un nuevo archivo **urls.py**

```py
from django.urls import path
from inicio.views import inicio

urlpatterns = [
    path('', inicio)
]
```

Para que el archivo **proyecto/urls.py** de la carpeta del proyecto reconozca los cambios de **incio/urls.py** de la aplicacion: Hay que agregar el siguiente path en el archivo proyecto/urls.py

```py
path('', include('inicio.urls'))
```

Dentro de ``Proyecto/settings.py`` - La opción:
**APP_DIRS: True,**
> Hace que detecte la carpeta 'templates' dentro de las aplicaciones.

## Modelos

### Consultar diferencia entre

- > ``python manage.py makemigrations``
Crea una migración de los modelos dentro de la aplicación.
- > ``python manage.py migrate``
Aplica las migraciones pendientes para todo el proyecto.

- models.Charfield(max_lenght=50)
