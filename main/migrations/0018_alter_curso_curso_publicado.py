# Generated by Django 3.2.5 on 2021-08-23 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_curso_curso_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 23, 15, 24, 28, 46529), verbose_name='fecha de publicacion'),
        ),
    ]
