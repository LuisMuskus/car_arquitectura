# Generated by Django 4.2.2 on 2023-06-17 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '__first__'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='cources_students',
            field=models.ManyToManyField(to='students.students'),
        ),
    ]
