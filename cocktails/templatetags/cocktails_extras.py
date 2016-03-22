from django import template
from cocktails.models import Cocktail

register = template.Library()

@register.inclusion_tag('cocktails/cocktail_list.html')
def get_cocktail_list():
    return {'cocktails': Cocktail.objects.all()}