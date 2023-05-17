# stockControl
Crear una entorno 

python -m venv env

Activar entorno

.\env\Scripts\activate


pip install Django==4.0

pip install jinja2

Crear un proyecto

django-admin startproject StockControl .

Crear una aplicación

python manage.py startapp compra

python manage.py makemigrations

Realizar migraciones
python manage.py migrate

#Abrir aplicación
python manage.py runserver 
