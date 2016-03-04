# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0018_auto_20160302_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeentry',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='entries',
            field=models.ManyToManyField(null=True, to='cocktails.RecipeEntry'),
        ),
    ]