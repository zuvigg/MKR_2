from django.db.models import Count  # Додайте імпорт Count

from django.shortcuts import render


def main(request):
    from books import models
    latest_recipes = models.Recipe.objects.order_by('-created_at')[:5]
    return render(request, 'recipe/main.html', {'latest_recipes': latest_recipes})

def category_list(request):
    from books import models
    categories = models.Category.objects.annotate(num_recipes=Count('recipes'))  # Використовуйте Count з django.db.models
    return render(request, 'recipe/category_list.html', {'categories': categories})