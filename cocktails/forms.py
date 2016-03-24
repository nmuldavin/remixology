from django import forms
from cocktails.models import *
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.forms.models import formset_factory

class CocktailForm (forms.ModelForm):
    name = forms.CharField()
    username = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name')
        username = cleaned_data.get('username')
        user = User.objects.get(username=username)
        slug = slugify(name)
        if Cocktail.objects.filter(name=name, user=user).exists():
            raise ValidationError('A cocktail with this name already exists! Choose another?')

        if Cocktail.objects.filter(slug=slug, user=user).exists():
            othername = Cocktail.objects.get(user=user, slug=slug)
            raise ValidationError(
                'The name you chose is too similar to the existing name \'%(othername)s\'. Choose another?',
                params={'othername': othername},
            )

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
