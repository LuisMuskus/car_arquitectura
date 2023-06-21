from django.shortcuts import render, HttpResponse, redirect
from django.template import Template, Context
from django.contrib.auth import login, logout
from django.contrib import messages
from car_architecture.tasks import process_excel_file
from car_architecture.tasks import process_excel_file_scrap
from django.views.decorators.csrf import csrf_exempt
import unittest
from apps.ratings.scrap import ScrapCourses



# Create your views here.

def home(request):
    return redirect("login")

@csrf_exempt
def index(request):
    template_base = open('./templates/index.html')
    template = Template(template_base.read())
    template_base.close()
    context = Context()
    content =  template.render(context)
    return HttpResponse(content)

def salir(request):
    logout(request)
    messages.success(request, F"Tu sesión fue cerrada correctamente")
    return redirect("login")

@csrf_exempt
def process_file(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']  # Obtiene el archivo de la solicitud
        file_path = 'excel_file.xlsx'
        with open(file_path, 'wb') as f:
            for chunk in excel_file.chunks():
                f.write(chunk)
        process_excel_file.delay(chunk)  # Envía el archivo a la tarea Celery para su procesamiento

    return render(request, 'index.html')

@csrf_exempt
def scraping_view(request):
    if request.method == 'POST':
        # Aquí puedes llamar a tu script de web scraping
        test_case = ScrapCourses.test_scrap_courses()
        file_path = "scrap_cursos.xlsx"
        process_excel_file_scrap.delay(file_path)  # Envía el archivo a la tarea Celery para su procesamiento
    return render(request, 'index.html')