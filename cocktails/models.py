from __future__ import unicode_literals

from django.contrib import admin
from django.template.defaultfilters import slugify
from django.db import models

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