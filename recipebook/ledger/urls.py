from django.urls import path
from .views import index, recipe_list

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipe_list, name='recipes/list') 
]
# This might be needed, depending on your Django version
app_name = "ledger"