# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-24 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0047_auto_20160324_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='recipes',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
