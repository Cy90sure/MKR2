from django.shortcuts import render
from .models import Recipe, Category

def main(request):
    latest_recipes = Recipe.objects.all().order_by('-created_at')[:5]
    return render(request, 'main.html', {'recipes': latest_recipes})

def category_list(request):
    categories = Category.objects.all()
    categories_with_count = []
    for category in categories:
        recipe_count = Recipe.objects.filter(category=category).count()
        categories_with_count.append({'category': category, 'count': recipe_count})
    return render(request, 'category_list.html', {'categories_with_count': categories_with_count})