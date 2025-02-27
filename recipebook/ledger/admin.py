from django.contrib import admin
from .models import Recipe

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', )

admin.site.register(Recipe, RecipeAdmin)
