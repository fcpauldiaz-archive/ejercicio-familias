# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 00:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0003_curso_integrantes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='integrantes',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]
