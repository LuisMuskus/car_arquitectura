# # tasks.py
# import pandas as pd
# from celery import shared_task
# from ..apps.students.models import Students

# @shared_task
# def importar_excel(datos):
#     # Procesar el archivo Excel utilizando pandas u otra biblioteca adecuada
#     # Acceder a los datos en el archivo y guardarlos en el modelo
#     df = pd.read_excel(datos)
#     # Procesar el DataFrame y guardar los datos en el modelo
#     for _, row in df.iterrows():
#         Students.objects.create(id_student=row['id_student'], name_student=row['name_student'], 
#                                 last_name_student=row['last_name_student'], age_student=row['age_student'], 
#                                 address_student=row['address_student'], email_student=row['email_student'])


# tasks.py
from celery import shared_task
from apps.students.models import Students
import os


import pandas as pd  # O cualquier otra librería que desees utilizar para procesar el archivo Excel

@shared_task
def process_excel_file(file_data):
    # Realiza las operaciones necesarias con el archivo Excel
    # Ejemplo: leer el archivo y guardar los datos en tu modelo Django
    df = pd.read_excel(file_data)  # Lee el archivo Excel usando pandas
    # Realiza las operaciones necesarias con los datos del
     # Procesar el DataFrame y guardar los datos en el modelo
    for _, row in df.iterrows():
        Students.objects.create(id_student=row['id_student'], name_student=row['name_student'],
                                last_name_student=row['last_name_student'], age_student=row['age_student'],
                                address_student=row['address_student'], email_student=row['email_student'])
    file_path = 'excel_file.xlsx'
    os.remove(file_path)

@shared_task
def add(x, y):
    return x + y

@shared_task
def multiply(x, y):
    return x * y
