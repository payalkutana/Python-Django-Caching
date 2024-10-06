from django.shortcuts import render
from cookbook.services import get_recipes
from django.views.decorators.cache import cache_page

@cache_page(60*2)
def recipes_view(request):
    recipe = get_recipes()
    for rec in recipe:
        print(rec)
        for ind in rec.ingredient.all():
            print("inside for ")
            print(ind.desc)
    print()
    return render(request, 'cookbook/recipes.html', {
        'recipes': get_recipes()
    })