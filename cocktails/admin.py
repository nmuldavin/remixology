from django.contrib import admin
from .models import Ingredient, Recipe, Cocktail, PurchasedIngredient



class IngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(PurchasedIngredient)

class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Recipe, RecipeAdmin)

class CocktailAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Cocktail, CocktailAdmin)