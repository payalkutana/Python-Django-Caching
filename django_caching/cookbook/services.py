from cookbook.models import Recipe


def get_recipes():
    # Queries 3 tables: cookbook_recipe, cookbook_ingredient,
    # and cookbook_food.
    return Recipe.objects.prefetch_related("ingredient")