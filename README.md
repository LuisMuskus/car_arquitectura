# car_arquitectura
Taller Car Arquitectura

Pasos para ejecutar el proyecto:

1. Instalar requirements.txt

2. car_arquitectura/car_architecture> python manage.py runserver

3. celery -A car_architecture worker --loglevel=info

4. redis-server

La base de datos utilizada es Sqlite.