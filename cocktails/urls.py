from django.conf.urls import url

from . import views

app_name='cocktails'

urlpatterns = [
    url(r'^ingredients/(?P<ingredient_slug>[-\w]+)/$', views.IngredientView.as_view(), name='ingredients'),
    url(r'^cocktails/(?P<cocktail_slug>[-\w]+)/$', views.GroupView.as_view(), name='cocktail'),
    url(r'^cocktails/(?P<cocktail_slug>[-\w]+)/(?P<rank>[0-9]+)/$', views.GetRecipe.as_view(), name='get_recipe')
]