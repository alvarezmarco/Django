
Crear la carpeta en /var/www en donde se alojará el proyecto
/var/www/virtual_environments# virtualenv .
Descargarse la aplicación 
/var/www/virtual_environments/virtual1# source bin/activate

(virtual1) root@kaliLinux:/var/www/virtual_environments/virtual1#pip install Django==1.11.3
Para conectarse a las base de datos
(virtual1) root@kaliLinux:/var/www/virtual_environments/virtual1# pip install psycopg2 

Configurar el archivo  ubicado en la carpeta mascotas/settings.py

ejemplo:
DATABASES = { 
    'default': { 
       
	'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'mascotas', # Nombre de la base de datos en PostreSQL
        'USER': '',  Nombre de Usuario 
        'PASSWORD': '', Contraseña
        'HOST': 'localhost', 
        'PORT': '5432', 
    } 
}

Se debe crear una base de datos en postgresq para este ejemplo mascotas y dentro de la carpeta ejecutar:
python manage.py migrate

python manage.py runserver

