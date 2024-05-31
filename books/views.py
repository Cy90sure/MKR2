from django.shortcuts import render
from .models import Book

def main(request):
    latest_books = Book.objects.all().order_by('-publication_date')[:5]
    return render(request, 'main.html', {'books': latest_books})

def category_list(request):
    categories = Book.objects.values('category').distinct()
    categories_with_count = []
    for category in categories:
        book_count = Book.objects.filter(category=category['category']).count()
        categories_with_count.append({'category': category['category'], 'count': book_count})
    return render(request, 'category_list.html', {'categories_with_count': categories_with_count})