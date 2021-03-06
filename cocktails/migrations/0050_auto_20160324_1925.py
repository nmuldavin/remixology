# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-24 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0049_userprofile_cocktails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
