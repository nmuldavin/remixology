from django.conf.urls import url

from . import views

app_name='cocktails'

urlpatterns = [
    url(r'^ingredients/', views.IngredientView.as_view(), name='ingredients')
]