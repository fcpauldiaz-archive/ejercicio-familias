# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0002_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='integrantes',
            field=models.ManyToManyField(to='families.Persona'),
        ),
    ]
