from django import template
from cocktails.models import Cocktail
from django.contrib.auth.models import User

register = template.Library()

@register.inclusion_tag('cocktails/user_cocktail_list.html')
def user_cocktail_list(user_directory, user):
    owner = User.objects.get(username=user_directory)
    return {'cocktails': Cocktail.objects.filter(user=owner), 'user_directory':user_directory, 'user':user}