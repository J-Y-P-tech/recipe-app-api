"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

# This will automatically create roots for the options in given view
from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
# This will create a new endpoint /recipes/
# and will assign all available endpoints from our
# RecipeViewSet to that endpoint.
# In other words it will have autogenerated URLs
# depending on the functionality that is enabled on the ViewSet
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
