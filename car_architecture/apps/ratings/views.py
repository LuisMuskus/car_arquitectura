from django.shortcuts import render, HttpResponse, redirect
from django.template import Template, Context
from django.contrib.auth import login, logout
from django.contrib import messages
from car_architecture.tasks import process_excel_file
from django.views.decorators.csrf import csrf_exempt
import unittest
from apps.ratings.tests import ScrapCourses



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

        
        # Realiza alguna acción con los resultados del web scraping
        test_case = ScrapCourses()

        test_result = test_case.run()

    resultados = {
        'total_pruebas': test_result.testsRun,
        'pruebas_fallidas': len(test_result.failures),
        'pruebas_errores': len(test_result.errors),
        'pruebas_omitidas': len(test_result.skipped),
        'resultados': test_result.tests,
    }

    #return render(request, 'resultados_prueba.html', {'resultados': resultados})
    return render(request, 'index.html')