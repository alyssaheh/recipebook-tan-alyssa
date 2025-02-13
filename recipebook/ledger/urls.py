from django.urls import path
from .views import index, recipe_list, recipe1

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipe_list, name='recipes/list'),
    path('recipe/1', recipe1, name='recipe/1') 
]
# This might be needed, depending on your Django version
app_name = "ledger"