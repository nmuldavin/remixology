from __future__ import unicode_literals

from django.contrib import admin
from django.template.defaultfilters import slugify
from django.db import models


# Models, progressing bottom level to top level . . .


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Ingredient, self).save(*args, **kwargs)

class IngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Ingredient, IngredientAdmin)

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)

class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Recipe, RecipeAdmin)


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

class CocktailAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Cocktail, CocktailAdmin)



