# Generated by Django 3.2.5 on 2021-08-19 21:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_curso_curso_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 16, 47, 38, 804753), verbose_name='fecha de publicacion'),
        ),
    ]
