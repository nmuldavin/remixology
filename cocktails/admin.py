from django.contrib import admin
from .models import Ingredient, IngredientInstance, Recipe, Cocktail



class IngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientInstance)

class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Recipe, RecipeAdmin)

class CocktailAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Cocktail, CocktailAdmin)