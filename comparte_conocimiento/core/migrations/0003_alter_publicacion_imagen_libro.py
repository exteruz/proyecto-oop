# Generated by Django 4.1.3 on 2022-11-26 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_publicacion_creador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='imagen_libro',
            field=models.ImageField(blank=True, upload_to='static/img/'),
        ),
    ]
