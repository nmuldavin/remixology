from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import *

class IngredientView(View):



    def get(self, request, *args, **kwargs):

        ctx = {}

        ingredient_slug = self.kwargs['ingredient_slug']

        try:
            ingredient = Ingredient.objects.get(slug=ingredient_slug)
            ctx['ingredient'] = ingredient

        except:
            pass

        return render(request, 'cocktails/ingredient.html', ctx)

class GroupView(View):

    def get(self, request, *args, **kwargs):

        ctx = {}

        if 'cocktail_slug' in self.kwargs:
            group_slug = self.kwargs['cocktail_slug']
            ctx['type'] = 'cocktail'
            try:
                group = Cocktail.objects.get(slug=group_slug)
                ctx['group'] = group
                print("Cocktail: " + group.name)
            except:
                pass

            try:
                recipe=Recipe.objects.get(cocktail=group, rank=1)
                ctx['recipe'] = recipe
                print("Recipe: " + recipe.label)
            except:
                pass

            try:
                ingredients=RecipeEntry.objects.filter(recipe=recipe).order_by('rank')
                print("it worked")
                ctx['ingredients'] = ingredients
                for entry in ingredients:
                    print(str(entry.rank) + ": " + entry.amount + "  " + entry.ingredient.name)
            except:
                pass



        return render(request, 'cocktails/recipegroup.html', ctx)


