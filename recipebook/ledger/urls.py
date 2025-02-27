from django.urls import path
from .views import index, RecipeListView

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
]

app_name = "ledger"