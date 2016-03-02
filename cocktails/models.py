from __future__ import unicode_literals
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

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super(Recipe, self).save(*args, **kwargs)