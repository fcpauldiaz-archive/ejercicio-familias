# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 00:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0004_auto_20161026_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CursoIntegrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignado_en', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='families.Curso')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='families.Persona')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='integrantes',
            field=models.ManyToManyField(through='families.CursoIntegrante', to='families.Persona'),
        ),
    ]
