from django import forms
from cocktails.models import Cocktail

class CocktailForm (forms.ModelForm):


    class Meta:
        model = Cocktail
        exclude = ('slug', 'type')
        widgets = {
            'description' : forms.Textarea(attrs={
                'placeholder' : 'Description'
            }),
        }

