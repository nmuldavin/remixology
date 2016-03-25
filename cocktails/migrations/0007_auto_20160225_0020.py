# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 00:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0006_remove_purchasedingredient_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasedingredient',
            name='brand',
        ),
        migrations.AddField(
            model_name='purchasedingredient',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
