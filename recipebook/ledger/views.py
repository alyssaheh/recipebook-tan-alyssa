from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from django.views.generic.list import ListView

# Create your views here.
def index(request):
    return HttpResponse('Please add /recipes/list to view recipes.')

def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes
    }
    return render(request, "recipe_list.html", context)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'