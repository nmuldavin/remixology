from django.contrib import admin
from .models import Ingredient, Recipe

class IngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Ingredient, IngredientAdmin)



class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("label",)}

admin.site.register(Recipe, RecipeAdmin)