from django.views.generic import DetailView, ListView
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = RecipeForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"


class RecipeCreateView(CreateView):
    model = Recipe
    fields = '__all__'
    template_name = 'recipe_form.html'
    success_url = "/recipes/list"

