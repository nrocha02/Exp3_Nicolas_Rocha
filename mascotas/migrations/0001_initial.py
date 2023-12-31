# Generated by Django 4.2.1 on 2023-06-17 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.IntegerField(max_length=5, primary_key=True, serialize=False, verbose_name='Codigo')),
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion')),
                ('precio', models.IntegerField(max_length=7, verbose_name='Precio')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Imagen')),
            ],
        ),
    ]
