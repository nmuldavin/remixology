from django.conf.urls import url

from . import views

app_name='cocktails'

urlpatterns = [
    url(r'^ingredients/(?P<ingredient_slug>[-\w]+)/$', views.IngredientView.as_view(), name='ingredients'),
    url(r'^cocktails/(addcocktail)/$', views.AddCocktail.as_view(), name='add_cocktail'),
    url(r'^cocktails/(?P<cocktail_slug>[-\w]+)/(?P<rank>[0-9]+)/$', views.GroupView.as_view(), name='cocktail'),
    url(r'^cocktails/(?P<cocktail_slug>[-\w]+)/$', views.GroupView.as_view(), name='cocktail'),
    url(r'^cocktails/(?P<cocktail_slug>[-\w]+)/(add_or_edit_recipe)/$', views.AddRecipe.as_view(), name='add_or_edit_recipe'),
    url(r'^cocktails/(?P<cocktail_slug>[-\w]+)/get_recipe/(?P<rank>[0-9]+)/$', views.RecipeView.as_view(), name='get_recipe')
]