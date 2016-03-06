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



        return render(request, 'cocktails/recipegroup.html', ctx)

class GetRecipe(View):

    def get(self, request, *args, **kwargs):

        ctx = {}
        if 'cocktail_slug' in self.kwargs:
            group_slug = self.kwargs['cocktail_slug']
            try:
                group = Cocktail.objects.get(slug=group_slug)
                print("Cocktail: " + group.name)
            except:
                pass

            print(group_slug)
            rank = self.kwargs['rank']
            try:
                recipe=Recipe.objects.get(cocktail=group, rank=rank)
                standard=Recipe.objects.get(cocktail=group, rank=1)
                print("Qoo")
                ctx['recipe'] = recipe
                print("Recipe: " + recipe.label)
            except:
                pass

            try:
                ingredients=RecipeEntry.objects.filter(recipe=recipe).order_by('rank')
                standardingredients=RecipeEntry.objects.filter(recipe=standard).order_by('rank')
                diffarray = []
                for entry, standardentry in zip(ingredients, standardingredients):
                    inner = []
                    inner.append(entry.rank==standardentry.rank)
                    inner.append(entry.amount==standardentry.amount)
                    inner.append(entry.ingredient.name==standardentry.ingredient.name)
                    print(inner)
                    print(str(entry.rank) + ": " + entry.amount + "  " + entry.ingredient.name)
                    diffarray.append(inner)
                zippedingredients = zip(ingredients, diffarray)
                ctx['ingredients'] = zippedingredients
            except:
                pass


        return render(request, 'cocktails/recipe.html', ctx)

