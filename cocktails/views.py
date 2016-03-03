from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import Ingredient

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

class CocktailView(View):

    def get(self, requesst, *args, **kwargs):

        return HttpResponse('it worked')

