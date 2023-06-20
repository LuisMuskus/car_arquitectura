from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.courses.models import Courses
from apps.students.models import Students


# Create your models here.

class Ratings(models.Model):
    min_rating = 0
    max_rating = 10
    rating = models.FloatField(verbose_name="Calificación",validators=[MinValueValidator(min_rating), MaxValueValidator(max_rating)],)
    courses_ratings = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Curso")
    students_ratings = models.ForeignKey(Students, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Estudiante",)

    def __str__(self):
        return self.courses_ratings.name_course  + " - " + self.students_ratings.name_student
    
    class Meta:
        verbose_name = 'CALIFICACIÓN'
        verbose_name_plural = 'CALIFICACIONES'