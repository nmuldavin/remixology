from django.conf.urls import url

from . import views

app_name='cocktails'

urlpatterns = [
    url(r'^ingredients/(?P<ingredient_slug>[-\w]+)', views.IngredientView.as_view(), name='ingredients')
]