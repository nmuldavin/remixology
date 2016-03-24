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


        user_directory = self.kwargs['user_directory']
        owner = User.objects.filter(username=user_directory)

        ctx['user_directory'] = user_directory


        if 'cocktail_slug' in self.kwargs:
            group_slug = self.kwargs['cocktail_slug']
            ctx['type'] = 'cocktail'
            try:
                group = Cocktail.objects.get(slug=group_slug, user=owner)

                ctx['group'] = group
                recipes = Recipe.objects.filter(cocktail=group).count()

                ctx['recipes'] = recipes
                ctx['recipes_range'] = range(1, recipes+1)

                if 'rank' in self.kwargs:
                    rank = int(self.kwargs['rank'])
                else:
                    rank = 1
                ctx['reciperank'] = rank
                if rank > recipes:
                        return HttpResponse('Error: ' + group.name + ' recipe number ' + str(rank) + ' does not exist!')
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
            user_directory = self.kwargs['user_directory']
            owner = User.objects.filter(username=user_directory)
            ctx['user_directory'] = user_directory
            try:
                group = Cocktail.objects.get(user=owner, slug=group_slug)
            except:
                print ("Error: Attempting to load recipe for nonexistent group")

            rank = self.kwargs['rank']

            ctx = LoadRecipe(group, rank)


        return render(request, 'cocktails/recipe.html', ctx)


def ProcessRecipeForm(user, cocktail, rank, recipe_form, entry_formset):
    Success = False
    if recipe_form.is_valid():
        recipe = recipe_form.save(commit=False)
        recipe.cocktail = cocktail
        recipe.user = user
        recipe.rank = rank
        if (Recipe.objects.filter(cocktail=cocktail, rank=rank).exists()):
            existing_recipe = Recipe.objects.get(cocktail=cocktail, rank=rank)
            existing_recipe.delete()
            print "Deleted old entry"
        recipe.save()

        if entry_formset.is_valid():
            Success = True
            entry_rank = 1
            for entry in entry_formset.forms:
                if entry.is_valid():

                    entry_object = Entry.objects.create(recipe=recipe)


                    entry_object.amount = entry.cleaned_data['amount']

                    entry_object.rank = entry_rank
                    entry_object.user = user
                    ingredient_name = entry.cleaned_data['ingredient']
                    #print(ingredient_name)

                    slug = slugify(ingredient_name)

                    if (Ingredient.objects.filter(user=user, slug=slug).exists()):
                        ingredient_object = Ingredient.objects.get(user=user, slug=slug)
                        ingredient_object.recipes += 1

                    else:
                        ingredient_object = Ingredient.objects.create(user=user, name=ingredient_name)
                        ingredient_object.recipes = 1

                    ingredient_object.save()
                    entry_object.ingredient = ingredient_object

                    entry_object.save()
                    #print(entry_rank)
                    entry_rank = entry_rank + 1
                else:
                    print "false"
                    print entry.errors


        else:
            recipe.delete()
            print entry_formset.errors

    else:
        print recipe_form.errors

    print(Success)
    if(Success):
        return {}
    else:
        return {'recipe_form':recipe_form, 'entry_formset':entry_formset}

class AddCocktail(View):

    def get(self, request, *args, **kwargs):
        ctx = {}
        ctx['rank'] = 1
        cocktail_form = CocktailForm(prefix='cocktail_form')
        ctx['cocktail_form'] = cocktail_form

        recipe_form = RecipeForm(prefix='recipe_form')
        ctx['recipe_form'] = recipe_form

        user_directory = self.kwargs['user_directory']
        ctx['user_directory'] = user_directory

        entry_formset = EntryFormSet(prefix='entry_formset')
        ctx['entry_formset'] = entry_formset

        return render(request, 'cocktails/addcocktail.html', ctx)

    def post(self, request, *args, **kwargs):
        cocktail_form = CocktailForm(request.POST, prefix='cocktail_form')
        recipe_form = RecipeForm(request.POST, prefix='recipe_form')
        user_directory = self.kwargs['user_directory']
        owner = User.objects.get(username=user_directory)
        init_formset = EntryFormSet(request.POST, prefix='entry_formset')
        numforms = init_formset.total_form_count()
        EntryFormSetVariation = formset_factory(EntryForm,
                                min_num=numforms,
                                validate_min=True,
                                can_delete=False,
                                extra=0)
        entry_formset = EntryFormSetVariation(request.POST, prefix='entry_formset')
        rank = 1
        if cocktail_form.is_valid():

            cocktail = cocktail_form.save(commit=False)
            cocktail.type = 'cocktial'
            cocktail.user = owner
            cocktail.save()
            recipe_form_response = ProcessRecipeForm(owner, cocktail, rank, recipe_form, entry_formset)

            if(not recipe_form_response):
                return redirect('cocktails:cocktail', user_directory=user_directory, cocktail_slug=cocktail.slug, rank=1)

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
        ctx['user_directory'] = user_directory

        return render(request, 'cocktails/addcocktail.html', ctx)



class AddRecipe(View):

    def get(self, request, *args, **kwargs):

        ctx = {}

        cocktail_slug = self.kwargs['cocktail_slug']
        ctx['cocktail_slug'] = cocktail_slug

        user_directory = self.kwargs['user_directory']
        ctx['user_directory'] = user_directory

        rank = int(self.kwargs['rank'])
        ctx['rank'] = rank

        recipe_form = RecipeForm(prefix='recipe_form')
        ctx['recipe_form'] = recipe_form

        entry_formset = EntryFormSet(prefix='entry_formset')
        ctx['entry_formset'] = entry_formset

        return render(request, 'cocktails/recipe_form.html', ctx)

    def post(self, request, *args, **kwargs):
        recipe_form = RecipeForm(request.POST, prefix='recipe_form')
        init_formset = EntryFormSet(request.POST, prefix='entry_formset')
        numforms = init_formset.total_form_count()
        EntryFormSetVariation = formset_factory(EntryForm,
                                min_num=numforms,
                                validate_min=True,
                                can_delete=False,
                                extra=0)
        entry_formset = EntryFormSetVariation(request.POST, prefix='entry_formset')
        cocktail_slug = self.kwargs['cocktail_slug']
        user_directory = self.kwargs['user_directory']
        owner = User.objects.get(username=user_directory)
        cocktail = Cocktail.objects.get(slug=cocktail_slug)

        rank = int(self.kwargs['rank'])

        recipe_form_response = ProcessRecipeForm(owner, cocktail, rank, recipe_form, entry_formset)

        if(not recipe_form_response):
            cocktail.recipes += 1
            return HttpResponse('saved')

        else:
            recipe_form = recipe_form_response['recipe_form']
            entry_formset = recipe_form_response['entry_formset']

        ctx = {}
        ctx['cocktail_slug'] = cocktail_slug
        ctx['rank'] = rank
        ctx['recipe_form'] = recipe_form
        ctx['entry_formset'] = entry_formset

        return render(request, 'cocktails/recipe_form.html', ctx)

class CocktailPage(View):

    def get(self, request, *args, **kwargs):
        ctx = {}
        user_directory = self.kwargs['user_directory']
        ctx['user_directory'] = user_directory
        owner = User.objects.get(username=user_directory)
        cocktails = Cocktail.objects.filter(user=owner).order_by('-recipes')
        ctx['cocktails'] = cocktails

        return render(request, 'cocktails/cocktail_page.html', ctx)