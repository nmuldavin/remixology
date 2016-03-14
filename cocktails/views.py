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

def LoadRecipe(cocktail, rank):

    ctx = {}

    try:
        recipe = Recipe.objects.get(cocktail=cocktail, rank=rank)
        ctx['recipe'] = recipe

    except:
        pass

    try:
        ingredients=Entry.objects.filter(recipe=recipe).order_by('rank')
        ctx['ingredients'] = ingredients

    except:
        pass

    return ctx

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

                if 'rank' in self.kwargs:
                    rank = int(self.kwargs['rank'])
                else:
                    rank = 1
                ctx['reciperank'] = rank

                recipectx = LoadRecipe(group, rank)
                ctx.update(recipectx)
            except:
                pass

        return render(request, 'cocktails/recipegroup.html', ctx)

class RecipeView(View):

    def get(self, request, *args, **kwargs):

        ctx = {}
        if 'cocktail_slug' in self.kwargs:
            group_slug = self.kwargs['cocktail_slug']
            try:
                group = Cocktail.objects.get(slug=group_slug)
            except:
                print ("Error: Attempting to load recipe for nonexistent group")

            rank = self.kwargs['rank']

            ctx = LoadRecipe(group, rank)


        return render(request, 'cocktails/recipe.html', ctx)


def ProcessRecipeForm(cocktail, rank, recipe_form, entry_formset):
    Success = False
    if recipe_form.is_valid():
        recipe = recipe_form.save(commit=False)
        recipe.cocktail = cocktail
        recipe.rank = rank
        recipe.save()

        if entry_formset.is_valid():
            Success = True
            entry_rank = 1

            for entry in entry_formset:
                if entry.is_valid():
                    entry_object = Entry.objects.create(recipe=recipe)

                    if 'amount' in entry.cleaned_data:
                        entry_object.amount = entry.cleaned_data['amount']

                    entry_object.rank = entry_rank
                    ingredient_name = entry.cleaned_data['ingredient']


                    slug = slugify(ingredient_name)

                    if (Ingredient.objects.filter(slug=slug).exists()):
                        ingredient_object = Ingredient.objects.get(slug=slug)
                        ingredient_object.recipes += 1

                    else:
                        ingredient_object = Ingredient.objects.create(name=ingredient_name)
                        ingredient_object.recipes = 1

                    ingredient_object.save()
                    entry_object.ingredient = ingredient_object

                    entry_object.save()

                    entry_rank = entry_rank + 1
                else:
                    print entry.errors


        else:
            print entry_formset.errors

    else:
        recipe.delete()
        print recipe_form.errors

    print(Success)
    if(Success):
        return {}
    else:
        return {'recipe_form':recipe_form, 'entry_formset':entry_formset}

class AddCocktail(View):

    def get(self, request, *args, **kwargs):

        ctx = {}
        cocktail_form = CocktailForm(prefix='cocktail_form')
        ctx['cocktail_form'] = cocktail_form

        recipe_form = RecipeForm(prefix='recipe_form')
        ctx['recipe_form'] = recipe_form

        entry_formset = EntryFormSet(prefix='entry_formset')
        ctx['entry_formset'] = entry_formset

        return render(request, 'cocktails/addcocktail.html', ctx)

    def post(self, request, *args, **kwargs):
        cocktail_form = CocktailForm(request.POST, prefix='cocktail_form')
        recipe_form = RecipeForm(request.POST, prefix='recipe_form')
        entry_formset = EntryFormSet(request.POST, prefix='entry_formset')
        rank = 1
        if cocktail_form.is_valid():

            cocktail = cocktail_form.save(commit=False)
            cocktail.type = 'cocktial'
            cocktail.save()
            recipe_form_response = ProcessRecipeForm(cocktail, rank, recipe_form, entry_formset)

            if(not recipe_form_response):
                return redirect('cocktails:cocktail', cocktail_slug='jet-pilot', rank=2)

            else:
                cocktail.delete()
                recipe_form = recipe_form_response['recipe_form']
                entry_formset = recipe_form_response['entry_formset']

        else:
            print cocktail_form.errors

        ctx = {}
        ctx['cocktail_form'] = cocktail_form
        ctx['recipe_form'] = recipe_form
        ctx['entry_formset'] = entry_formset

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




