from django import template
from cocktails.models import Cocktail
from django.contrib.auth.models import User

register = template.Library()

@register.inclusion_tag('cocktails/cocktail_list.html')
def get_cocktail_list(user_directory):
    user = User.objects.get(username=user_directory)
    return {'cocktails': Cocktail.objects.filter(user=user), 'user_directory':user_directory}