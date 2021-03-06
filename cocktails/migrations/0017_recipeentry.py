# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0016_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(blank=True, max_length=30)),
                ('ingredient', models.ManyToManyField(to='cocktails.Ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocktails.Recipe')),
            ],
        ),
    ]
