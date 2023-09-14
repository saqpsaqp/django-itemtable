# Descripción

Esta es un aplicacion de prueba que agrega un item con la fecha y hora actual (horas y minutos)
que no permite que se repita. usando datatables y con las opciones de editar, eliminar (logicamente),
activar o desactivar (estado) y utilizando clases de vista de Django.

# Ejecución

1. Crear un entorno virtual (utilizando VirtualEnWrapper):

<code>
    mkvirtualenv itemtable
</code>

2. Instalar dependencias:

<code>
    pip install -r requirements.txt
</code>

3. Ejecutar migraciones y crear usuario admin

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

4. Abrir el Navegador http://localhost:8000