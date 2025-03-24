from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy

from .models import Recipe, RecipeImage
from .forms import RecipeForm


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
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['name']
    template_name = 'recipe_form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_title'] = "Create a New Recipe"
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ledger:recipe-detail', kwargs={'pk': self.object.pk})


class RecipeImageView(CreateView):
    model = RecipeImage
    fields = ['image', 'description']
    template_name = 'recipe_form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_title'] = "Upload an Image"
        ctx['recipe'] = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        return ctx

    def form_valid(self, form):
        form.instance.recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ledger:recipe-detail', kwargs={'pk': self.kwargs['pk']})
