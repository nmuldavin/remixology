from django import forms
from cocktails.models import *
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.forms.models import inlineformset_factory

def validate_name_and_slug(name):
    if Cocktail.objects.filter(name=name).exists():
        raise ValidationError('A cocktial with this name already exists! Choose another?')
    slug = slugify(name)
    if Cocktail.objects.filter(slug=slug).exists():
        othername = Cocktail.objects.get(slug=slug)
        raise ValidationError(
                'The name you chose is too similar to the existing name \'%(othername)s\'. Choose another?',
            params={'othername': othername},
        )

class CocktailForm (forms.ModelForm):
    name = forms.CharField(validators=[validate_name_and_slug])

    class Meta:
        model = Cocktail
        exclude = ('slug', 'type')

class EntryForm (forms.ModelForm):
    amount = forms.CharField()
    ingredient = forms.CharField()
    class Meta:
        exclude = ('rank', 'recipe')

EntryFormSet = inlineformset_factory(Recipe,
                                     Entry,
                                     form=EntryForm,
                                     fields=('amount', 'ingredient',),
                                     can_delete=False,
                                     extra=5)



class RecipeForm (forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ('cocktail', 'rank')
