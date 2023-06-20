from django.db import models
from apps.teachers.models import Teachers
from apps.students.models import Students
# Create your models here.

class Courses(models.Model):
    id_course = models.IntegerField(verbose_name="Id",unique=True, null=True)
    name_course = models.CharField(verbose_name="Nombre",max_length=50, null=True)
    description_course = models.TextField(verbose_name="Descripción",null=True)
    cources_students = models.ManyToManyField(Students, blank=True, verbose_name="Estudiante")
    course_teacher = models.OneToOneField(Teachers, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Profesor")
    
    def __str__(self):
        return self.name_course
    
    class Meta:
        verbose_name = 'CURSO'
        verbose_name_plural = 'CURSOS'