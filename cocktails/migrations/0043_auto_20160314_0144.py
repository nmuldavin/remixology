# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0042_ingredient_recipes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='label',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
