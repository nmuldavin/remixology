# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 23:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0025_recipe_index'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cocktail',
            new_name='RecipeGroup',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='cocktail',
            new_name='group',
        ),
    ]
