# Generated by Django 4.2.2 on 2023-06-17 19:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_courses_cources_students_and_more'),
        ('students', '0005_alter_students_address_student_and_more'),
        ('ratings', '0002_alter_ratings_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='courses_ratings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='id_rating',
            field=models.IntegerField(unique=True, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Calificación'),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='students_ratings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.students', verbose_name='Estudiante'),
        ),
    ]
