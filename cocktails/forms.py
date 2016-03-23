from django import forms
from cocktails.models import *
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.forms.models import formset_factory

def validate_name_and_slug(name):
    if Cocktail.objects.filter(name=name).exists():
        raise ValidationError('A cocktail with this name already exists! Choose another?')
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
        exclude = ('slug', 'type', 'user')


def nullValidation(amount):
    if(False):
        raise(ValidationError('This will never happen'))

class EntryForm (forms.Form):
    amount = forms.CharField(required=False)
    ingredient = forms.CharField(required=True)

    class Meta:
        fields = ('amount', 'ingredient')


EntryFormSet = formset_factory(EntryForm,
                                min_num=2,
                                validate_min=True,
                                can_delete=False,
                                extra=0)

class RecipeForm (forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ('cocktail', 'rank')
