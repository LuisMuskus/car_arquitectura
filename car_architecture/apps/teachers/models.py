from django.db import models

# Create your models here.

class Teachers(models.Model):
    id_teacher = models.IntegerField(verbose_name="Número de identificación",unique=True, null=True)
    name_teacher = models.CharField(verbose_name="Nombre",max_length=20, null=True)
    last_name_teacher= models.CharField(verbose_name="Apellido",max_length=20, null=True)
    age_teacher= models.IntegerField(verbose_name="Edad",null=True)
    address_teacher = models.CharField(verbose_name="Dirección",max_length=200, null=True)
    email_teacher = models.EmailField(verbose_name="Email",max_length = 254, null=True)

    def __str__(self):
        return self.name_teacher
    
    class Meta:
        verbose_name = 'PROFESOR'
        verbose_name_plural = 'PROFESORES'