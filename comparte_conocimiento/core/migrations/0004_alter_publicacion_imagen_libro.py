# Generated by Django 4.1.3 on 2022-11-26 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_publicacion_imagen_libro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='imagen_libro',
            field=models.ImageField(blank=True, default='static/img/img_default.png', upload_to='static/img/'),
        ),
    ]
