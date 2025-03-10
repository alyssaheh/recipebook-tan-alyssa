from django.views.generic import DetailView, ListView
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"
