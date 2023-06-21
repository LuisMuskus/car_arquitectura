# tasks.py
from celery import shared_task
from apps.students.models import Students
from apps.courses.models import Courses
from apps.teachers.models import Teachers
from apps.ratings.models import Ratings
from apps.courses.models import Courses
import pandas as pd 

@shared_task
def process_excel_file(file_data):
    #Dataframe para Estudiantes
    df_students = pd.read_excel(file_data)  # Lee el archivo Excel usando pandas
    # Realiza las operaciones necesarias con los datos del
     # Procesar el DataFrame y guardar los datos en el modelo
    for _, row in df_students.iterrows():
        Students.objects.create(id_student=row['id_student'], name_student=row['name_student'],
                                last_name_student=row['last_name_student'], age_student=row['age_student'],
                                address_student=row['address_student'], email_student=row['email_student'])
        
    # #Dataframa para Profesores
    # df_teachers = pd.read_excel(file_data, sheet_name='profesores')  # Lee el archivo Excel usando pandas
    # # Realiza las operaciones necesarias con los datos del
    #  # Procesar el DataFrame y guardar los datos en el modelo
    # for _, row in df_teachers.iterrows():
    #     Teachers.objects.create(id_teacher=row['id_teacher'], name_teacher=row['name_teacher'],
    #                             last_name_teacher=row['last_name_teacher'], age_teacher=row['age_teacher'],
    #                             address_teacher=row['address_teacher'], email_teacher=row['email_teacher'])
        
    # #DataFrame para Cursos
    # df_courses = pd.read_excel(file_data, sheet_name='cursos')  # Lee el archivo Excel usando pandas
    # # Realiza las operaciones necesarias con los datos del
    #  # Procesar el DataFrame y guardar los datos en el modelo
    # for _, row in df_courses.iterrows():
    #     Courses.objects.create(id_course=row['id_course'], name_course =row['name_course '],
    #                             description_course=row['description_course'], cources_students=row['cources_students'],
    #                             course_teacher=row['course_teacher']
    #                             )
    
    
    # #DataFrame para Calificaiones
    # df_ratings = pd.read_excel(file_data, sheet_name='calificaciones')  # Lee el archivo Excel usando pandas
    # # Realiza las operaciones necesarias con los datos del
    #  # Procesar el DataFrame y guardar los datos en el modelo
    # for _, row in df_ratings.iterrows():
    #     Ratings.objects.create(rating=row['rating'], courses_ratings=row['courses_ratings'],
    #                             students_ratings=row['students_ratings'])


@shared_task
def process_excel_file_scrap(file_data):
    df = pd.read_excel(file_data)  # Lee el archivo Excel usando pandas
    # Realiza las operaciones necesarias con los datos del
     # Procesar el DataFrame y guardar los datos en el modelo
    for _, row in df.iterrows():
        Courses.objects.create(name_course=row['name_course'], description_course=row['description_course'])
