from django.contrib import admin
from .models import Ingredient, Recipe, RecipeEntry, Cocktail




class IngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class IngredientInLine(admin.TabularInline):
    model = Ingredient
    prepopulated_fields = {"slug": ("name",)}

class RecipeEntryInLine(admin.TabularInline):
    model = RecipeEntry
    inlines = [
        IngredientInLine
    ]

class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("label",)}
    inlines = [
        RecipeEntryInLine,
    ]

class CocktailAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slug": ("name",)}

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Cocktail, CocktailAdmin)
