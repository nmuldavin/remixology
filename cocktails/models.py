from __future__ import unicode_literals

from django.template.defaultfilters import slugify
from django_measurement.models import MeasurementField
from measurement.measures import Volume
from django.db import models


# Models, progressing bottom level to top level . . .


# Ingredient class, encompasing overall ingredient name. Each ingredient
# can include as many individual ingredient instances as it wants.
class Ingredient(models.Model):

    # from django examples. Fill in later with ingredient type choices,
    # maybe take from pdt app or elsewhere. Investigate types and subtypes.
    MEDIA_CHOICES = (
        ('Audio', (
                ('vinyl', 'Vinyl'),
                ('cd', 'CD'),
            )
        ),
        ('Video', (
                ('vhs', 'VHS Tape'),
                ('dvd', 'DVD'),
            )
        ),
        ('unknown', 'Unknown'),
    )

    name = models.CharField(max_length=50)
    slug = models.SlugField(default='', blank=True)
    type = models.CharField(max_length=2, choices=MEDIA_CHOICES, blank=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Ingredient, self).save(*args, **kwargs)

class IngredientInstance(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,)

    class Meta:
        abstract = True

class PurchasedIngredient(IngredientInstance):
    product = models.CharField(default='', max_length = 100)
    notes = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    volume = MeasurementField(measurement=Volume, null=True)

    def __str__(self):
        return self.ingredient.name + " - " + self.product



class Recipe(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)

# cocktail class, containing a list of recipes, variations, and notes as well
# as a log of each time the cocktail was made and in what context
class Cocktail(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Cocktail, self).save(*args, **kwargs)




