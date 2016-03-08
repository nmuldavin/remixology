import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remixology.settings')

import django
django.setup()

from cocktails.models import *

def AddCocktail(name, description, notes):
    c = Cocktail.objects.get_or_create(name=name)[0]
    c.description = description
    c.notes = notes
    c.save()
    return c

def AddRecipe(group, label, directions, notes, rank):
    r = Recipe.objects.get_or_create(cocktail=group, rank=rank)[0]
    r.label = label
    r.directions = directions
    r.notes = notes
    r.save()
    return r

def AddEntry(recipe, rank, amount, ingredient):
    e = RecipeEntry.objects.get_or_create(recipe = recipe, rank=rank)[0]
    e.amount = amount
    e.ingredient = ingredient
    e.save()
    return e

def AddIngredient(name):
    i = Ingredient.objects.get_or_create(name=name)[0]
    i.save()
    return i

def populate():
    c = AddCocktail('Jet Pilot', 'Spicy and Strong', 'Standard recipe courtesy of Beachbum Berry')
    r = AddRecipe(c, 'Standard', 'Shake with crushed ice, then pour mixture in to chilled glass.',
                  'The standard recipe is very solid but sometimes needs to be tweaked', 1)
    e = AddEntry(r, 1, '1 oz', AddIngredient('Dark Jamaican Rum'))
    e = AddEntry(r, 2, '3/4 oz', AddIngredient('Gold Puerto Rican Rum'))
    e = AddEntry(r, 3, '3/4 oz', AddIngredient('Overproof Demerara Rum'))
    e = AddEntry(r, 3, '1/2 oz', AddIngredient('Cinnamon Syrup'))
    e = AddEntry(r, 4, '1/2 oz', AddIngredient('Falernum'))
    e = AddEntry(r, 5, '1/2 oz', AddIngredient('Lime Juice'))
    e = AddEntry(r, 6, '1/2 oz', AddIngredient('Grapefruit Juice'))
    e = AddEntry(r, 7, '6 Drops', AddIngredient('Pernod'))
    e = AddEntry(r, 8, '1 Dash', AddIngredient('Angostura Bitters'))
    e = AddEntry(r, 9, '', AddIngredient('Crushed Ice'))

    r = AddRecipe(c, 'Hale Pele', 'Shake with crushed ice, then pour mixture in to chilled glass.',
                  'The standard recipe is very solid but sometimes needs to be tweaked', 2)
    e = AddEntry(r, 1, '1 oz', AddIngredient('Blackstrap Rum'))
    e = AddEntry(r, 2, '1 oz', AddIngredient('Gold Puerto Rican Rum'))
    e = AddEntry(r, 3, '3/4 oz', AddIngredient('Overproof Demerara Rum'))
    e = AddEntry(r, 3, '1/2 oz', AddIngredient('Cinnamon Syrup'))
    e = AddEntry(r, 4, '1/2 oz', AddIngredient('Falernum'))
    e = AddEntry(r, 5, '1/2 oz', AddIngredient('Lime Juice'))
    e = AddEntry(r, 6, '1/2 oz', AddIngredient('Grapefruit Juice'))
    e = AddEntry(r, 7, '6 Drops', AddIngredient('Pernod'))
    e = AddEntry(r, 8, '1 Dash', AddIngredient('Angostura Bitters'))
    e = AddEntry(r, 9, '', AddIngredient('Crushed Ice'))






if __name__ == '__main__':
    print "Starting population script..."
    populate()




