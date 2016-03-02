from django.contrib import admin
from .models import Ingredient, Recipe, RecipeEntry




class IngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Ingredient, IngredientAdmin)

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

admin.site.register(Recipe, RecipeAdmin)