from django.urls import path
from .views import recipes_view

urlpatterns = [
    path("recipes/", recipes_view, name="get-recipes"),
]

