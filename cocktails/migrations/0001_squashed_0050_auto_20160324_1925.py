# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 00:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [(b'cocktails', '0001_initial'), (b'cocktails', '0002_auto_20160224_2256'), (b'cocktails', '0003_ingredientinstance'), (b'cocktails', '0004_auto_20160225_0007'), (b'cocktails', '0005_auto_20160225_0013'), (b'cocktails', '0006_remove_purchasedingredient_name'), (b'cocktails', '0007_auto_20160225_0020'), (b'cocktails', '0008_purchasedingredient_volume'), (b'cocktails', '0009_auto_20160225_0134'), (b'cocktails', '0010_purchasedingredient_price'), (b'cocktails', '0011_homemadeingredient'), (b'cocktails', '0012_auto_20160225_0353'), (b'cocktails', '0013_auto_20160225_0359'), (b'cocktails', '0014_auto_20160302_1747'), (b'cocktails', '0015_ingredient'), (b'cocktails', '0016_recipe'), (b'cocktails', '0017_recipeentry'), (b'cocktails', '0018_auto_20160302_1938'), (b'cocktails', '0019_auto_20160302_2022'), (b'cocktails', '0020_auto_20160302_2029'), (b'cocktails', '0021_auto_20160302_2032'), (b'cocktails', '0022_cocktail'), (b'cocktails', '0023_recipe_cocktail'), (b'cocktails', '0024_recipeentry_rank'), (b'cocktails', '0025_recipe_index'), (b'cocktails', '0026_auto_20160303_2325'), (b'cocktails', '0027_recipegroup_type'), (b'cocktails', '0028_auto_20160304_0134'), (b'cocktails', '0029_auto_20160304_1652'), (b'cocktails', '0030_cocktail_description'), (b'cocktails', '0031_cocktail_notes'), (b'cocktails', '0032_auto_20160304_1911'), (b'cocktails', '0033_auto_20160304_1953'), (b'cocktails', '0034_auto_20160304_2227'), (b'cocktails', '0035_auto_20160310_0448'), (b'cocktails', '0036_auto_20160310_0506'), (b'cocktails', '0037_auto_20160310_0512'), (b'cocktails', '0038_auto_20160310_0523'), (b'cocktails', '0039_auto_20160310_0526'), (b'cocktails', '0040_auto_20160310_2140'), (b'cocktails', '0041_auto_20160313_1700'), (b'cocktails', '0042_ingredient_recipes'), (b'cocktails', '0043_auto_20160314_0144'), (b'cocktails', '0044_userprofile'), (b'cocktails', '0045_auto_20160323_1633'), (b'cocktails', '0046_cocktail_public'), (b'cocktails', '0047_auto_20160324_1619'), (b'cocktails', '0048_cocktail_recipes'), (b'cocktails', '0049_userprofile_cocktails'), (b'cocktails', '0050_auto_20160324_1925')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
                ('recipes', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='', max_length=100)),
                ('slug', models.SlugField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(blank=True, max_length=30)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocktails.Recipe')),
                ('ingredient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cocktails.Ingredient')),
                ('rank', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='directions',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='rank',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150, unique=True)),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
                ('type', models.CharField(default='cocktail', max_length=30)),
                ('description', models.TextField(blank=True, max_length=140)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='cocktail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cocktails.Cocktail'),
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='slug',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='label',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='recipe',
            unique_together=set([('cocktail', 'rank')]),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cocktails', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='cocktail',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='recipes',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterUniqueTogether(
            name='cocktail',
            unique_together=set([('user', 'name'), ('user', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='ingredient',
            unique_together=set([('user', 'name'), ('user', 'slug')]),
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
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
