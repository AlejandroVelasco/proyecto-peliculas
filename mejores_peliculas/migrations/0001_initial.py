# Generated by Django 4.2.5 on 2023-10-26 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('duracion', models.IntegerField()),
                ('quote', models.CharField(max_length=200)),
                ('imagen', models.CharField(max_length=200)),
                ('sinopsis', models.CharField(max_length=2000)),
                ('votos', models.IntegerField()),
            ],
        ),
    ]
