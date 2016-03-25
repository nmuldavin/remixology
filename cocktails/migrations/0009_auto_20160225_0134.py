# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 01:34
from __future__ import unicode_literals

from django.db import migrations
import django_measurement.models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0008_purchasedingredient_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedingredient',
            name='volume',
            field=django_measurement.models.MeasurementField(measurement_class='Volume', null=True),
        ),
    ]
