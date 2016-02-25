from django.contrib import admin
from .models import Ingredient, Recipe, Cocktail, PurchasedIngredient, HomemadeIngredient



class IngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(PurchasedIngredient)
admin.site.register(HomemadeIngredient)

class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("descriptor",)}

admin.site.register(Recipe, RecipeAdmin)

class CocktailAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Cocktail, CocktailAdmin)
