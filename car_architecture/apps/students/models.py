from django.db import models

# Create your models here.

class Students(models.Model):
    id_student = models.IntegerField(verbose_name="Número de identificación",unique=True, null=True)
    name_student = models.CharField(verbose_name="Nombre",max_length=20, null=True)
    last_name_student = models.CharField(verbose_name="Apellido",max_length=20, null=True)
    age_student = models.IntegerField(verbose_name="Edad",null=True)
    address_student = models.CharField(verbose_name="Dirección",max_length=200, null=True)
    email_student = models.EmailField(verbose_name="email",max_length = 254, null=True)

    def __str__(self):
        return self.name_student
    
    class Meta:
        verbose_name = 'ESTUDIANTE'
        verbose_name_plural = 'ESTUDIANTES'