# Generated by Django 3.2.5 on 2021-08-17 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0003_alter_inscripcion_fecha_inscripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='fecha_inscripcion',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 17, 16, 29, 45, 213154), verbose_name='fecha de publicacion'),
        ),
    ]
