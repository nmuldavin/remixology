from django.conf.urls import url

from . import views

app_name='cocktails'

urlpatterns = [
    url(r'^(?P<user_directory>[-\w]+)/ingredients/(?P<ingredient_slug>[-\w]+)/$', views.IngredientView.as_view(), name='ingredients'),
    url(r'^(?P<user_directory>[-\w]+)/cocktails/$', views.CocktailPage.as_view(), name='cocktail_page'),
    url(r'^(?P<user_directory>[-\w]+)/cocktails/addcocktail/$', views.AddCocktail.as_view(), name='add_cocktail'),
    url(r'^(?P<user_directory>[-\w]+)/cocktails/(?P<cocktail_slug>[-\w]+)/(?P<rank>[0-9]+)/$', views.GroupView.as_view(), name='cocktail'),
    url(r'^(?P<user_directory>[-\w]+)/cocktails/(?P<cocktail_slug>[-\w]+)/$', views.GroupView.as_view(), name='cocktail'),
    url(r'^(?P<user_directory>[-\w]+)/cocktails/(?P<cocktail_slug>[-\w]+)/(add_or_edit_recipe)/(?P<rank>[0-9]+)/$', views.AddRecipe.as_view(), name='add_or_edit_recipe'),
    url(r'^(?P<user_directory>[-\w]+)/cocktails/(?P<cocktail_slug>[-\w]+)/get_recipe/(?P<rank>[0-9]+)/$', views.RecipeView.as_view(), name='get_recipe')
]