# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-16 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customizer', '0001_initial'),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='only_competition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Competition'),
        ),
    ]
