from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from django.template.defaultfilters import slugify
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
        ctx = {}
        cocktailform = CocktailForm(prefix='cocktail_form')
        ctx['cocktailform'] = cocktailform
        recipeform = RecipeForm(prefix='recipe_form')
        ctx['recipeform'] = recipeform
        entry_formset = EntryFormSet(prefix='entry_formset')
        ctx['entry_formset'] = entry_formset
        return render(request, 'cocktails/addcocktail.html', ctx)

    def post(self, request, *args, **kwargs):
        cocktailform = CocktailForm(request.POST, prefix='cocktail_form')

        if cocktailform.is_valid():

            cocktail = cocktailform.save(commit=True)
            cocktail.type = 'cocktial'
            cocktail.save()
            ctx = AddRecipe.as_view()(self.request, **{'cocktail':cocktail})
            ctx = dict(ctx.items() + {'cocktailform':cocktailform}.items())

        else:
            print cocktailform.errors

        return render(request, 'cocktails/addcocktail.html', ctx)

class AddRecipe(View):

    def get(self, request, *args, **kwargs):
        recipeform = RecipeForm(prefix='recipe_form')
        entry_formset = EntryFormSet(prefix='entry_formset')
        return render(request, 'cocktails/recipeform.html', {
            'recipeform': recipeform,
            "entry_formset" : entry_formset
        })
        #return render(request, 'cocktails/recipeform.html', {'recipeform':recipeform})

    def post(self, request, *args, **kwargs):
        # get and save recipe form
        recipeform = RecipeForm(request.POST, prefix='recipe_form')
        entry_formset = EntryFormSet(request.POST, prefix='entry_formset')
        recipe = recipeform.save(commit=False)
        if recipeform.is_valid():

            # get cocktail reference form kwargs:
            if 'cocktail' in self.kwargs:
                cocktail = self.kwargs['cocktail']
                recipe.cocktail = cocktail
            else:
                return HttpResponse('Error: recipe not assigned to a group object.')

            if 'rank' in self.kwargs:
                recipe.rank= int(self.kwargs['rank'])

            recipe.save()

            if entry_formset.is_valid():

                rank = 1

                for entry in entry_formset:

                    entryobject = Entry.objects.create(recipe=recipe)

                    entryobject.amount = entry.cleaned_data['amount']

                    entryobject.rank = rank

                    ingredientname = entry.cleaned_data['ingredient']

                    slug = slugify(ingredientname)

                    if (Ingredient.objects.filter(slug=slug).exists()):
                        ingredientobject = Ingredient.objects.get(slug=slug)
                        ingredientobject.recipes += 1

                    else:
                        ingredientobject = Ingredient.objects.create(name=ingredientname)
                        ingredientobject.recipes = 1

                    ingredientobject.save()
                    entryobject.ingredient = ingredientobject

                    entryobject.save()

                    rank = rank + 1

            else:
                print entry_formset.errors

        else:
            print recipeform.errors


        return {'recipeform':recipeform, 'entry_formset':entry_formset}




