from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(default='', blank=True, unique=True)
    recipes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Ingredient, self).save(*args, **kwargs)

    class Meta:
        unique_together = (('user', 'name'), ('user', 'slug'))

# Ingredient entry model, my "it-will-work-for-now" method of getting
# a 2-D array of ingredients and amounts in to the recipe class. The
# IngredientEntry class contains a spot for an ingredient and a spot for
# the amount. It will have a many-to-one relationship with a single recipe.
# This is pretty inefficient but the django postgressQL array field type
# does not allow relational entries as a base field. Eventually it would be good
# to find a better way of storing this data.
class Entry(models.Model):
    user = models.ForeignKey(User, null=True)
    rank = models.IntegerField(default=0)
    amount = models.CharField(max_length=30, blank=True)
    ingredient = models.ForeignKey(Ingredient, null=True)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

# Recipe model
class Recipe(models.Model):
    user = models.ForeignKey(User, null=True)
    label = models.CharField(blank=True, max_length=100)
    directions = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    cocktail = models.ForeignKey('cocktail', null=True, on_delete=models.CASCADE)
    rank = models.IntegerField(default=1)

    class Meta:
        unique_together = ('cocktail', 'rank')

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super(Recipe, self).save(*args, **kwargs)

class RecipeGroup(models.Model):
    name = models.CharField(default='', max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(default='', blank=True)
    type = models.CharField(default='cocktail', max_length=30)
    public = models.BooleanField(default=False)
    description = models.TextField(max_length=140, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(RecipeGroup, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        unique_together = (('user', 'name'), ('user', 'slug'))


class Cocktail(RecipeGroup):
    type='cocktail'
    pass