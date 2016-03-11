from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from .models import *
from .forms import *
from django.template import RequestContext

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
                recipes = Recipe.objects.filter(cocktail=group).count()
                ctx['recipes'] = recipes
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
            except:
                pass

            rank = self.kwargs['rank']
            try:
                recipe=Recipe.objects.get(cocktail=group, rank=rank)
                ctx['recipe'] = recipe
            except:
                pass

            try:
                ingredients=Entry.objects.filter(recipe=recipe).order_by('rank')
                ctx['ingredients'] = ingredients

            except:
                pass


        return render(request, 'cocktails/recipe.html', ctx)

class AddCocktail(View):

    def get(self, request, *args, **kwargs):
        cocktailform = CocktailForm()

        return render(request, 'cocktails/addcocktail.html', {'cocktailform': cocktailform})

    def post(self, request, *args, **kwargs):
        cocktailform = CocktailForm(request.POST)


        if cocktailform.is_valid():

            cocktail = cocktailform.save(commit=True)
            cocktail.type = 'cocktial'
            cocktail.save()

            return redirect ('cocktails:cocktail', cocktail_slug=cocktail.slug)

        else:
            print form.errors

        return render(request, 'cocktails/addcocktail.html', {'cocktailform': cocktailform})

class AddRecipe(View):

    def get(self, request, *args, **kwargs):
        recipeform = RecipeForm()
        entry_formset = EntryFormSet(instance=Recipe())
        return render(request, 'cocktails/recipeform.html', {
            'recipeform': recipeform,
            "entry_formset" : entry_formset
        }, context_instance=RequestContext(request))



