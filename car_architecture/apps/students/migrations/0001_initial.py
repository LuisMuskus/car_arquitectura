# Generated by Django 4.2.2 on 2023-06-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_student', models.IntegerField(null=True, unique=True)),
                ('name_student', models.CharField(max_length=20, null=True)),
                ('last_name_student', models.CharField(max_length=20, null=True)),
                ('age_student', models.IntegerField(null=True)),
                ('address_student', models.CharField(max_length=200, null=True)),
                ('email_student', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]