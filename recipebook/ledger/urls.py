from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeImageView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe-form'),
    path('recipe/<int:pk>/add_image', RecipeImageView.as_view(), name='add-image'),  
]

app_name = "ledger"
