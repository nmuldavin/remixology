from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models



# ingredient model. Contains a name and slug field
class Ingredient(models.Model):

    TYPE_CHOICES = (
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

    name = models.CharField(max_length=100)
    slug = models.SlugField(default='', blank=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Ingredient, self).save(*args, **kwargs)


# Recipe model
class Recipe(models.Model):
    label = models.CharField(default='', max_length=100)
    slug = models.SlugField(default='', blank=True)
    directions = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    cocktail = models.ForeignKey('cocktail', null=True, on_delete=models.CASCADE)
    rank = models.IntegerField(default=1)

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super(Recipe, self).save(*args, **kwargs)


# Ingredient entry model, my "it-will-work-for-now" method of getting
# a 2-D array of ingredients and amounts in to the recipe class. The
# IngredientEntry class contains a spot for an ingredient and a spot for
# the amount. It will have a many-to-one relationship with a single recipe.
# This is pretty inefficient but the django postgressQL array field type
# does not allow relational entries as a base field. Eventually it would be good
# to find a better way of storing this data.
class RecipeEntry(models.Model):
    rank = models.IntegerField(default=0)
    amount = models.CharField(max_length=30, blank=True)
    ingredient = models.ForeignKey(Ingredient, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class RecipeGroup(models.Model):
    name = models.CharField(default='', max_length=150)
    slug = models.SlugField(default='', blank = True)
    type = models.CharField(default='cocktail', max_length=30)
    description = models.TextField(max_length=140, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(RecipeGroup, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class Cocktail(RecipeGroup):
    pass