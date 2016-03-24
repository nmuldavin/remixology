from django.contrib import admin
from .models import Ingredient, Recipe, Entry, Cocktail, UserProfile




class IngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class IngredientInLine(admin.TabularInline):
    model = Ingredient
    prepopulated_fields = {"slug": ("name",)}

class EntryInLine(admin.TabularInline):
    model = Entry
    inlines = [
        IngredientInLine
    ]

class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        EntryInLine,
    ]

class CocktailAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slug": ("name",)}

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(UserProfile)
