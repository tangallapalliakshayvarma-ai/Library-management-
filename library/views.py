from django.shortcuts import render, redirect
from .models import Book
from django.db.models import Q

def home(request):
    return render(request, 'index.html')

def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        isbn = request.POST.get("isbn")
        if title and author and isbn:
            Book.objects.create(title=title, author=author, isbn=isbn)
        return redirect('view_books')
    return render(request, 'add_book.html')

def view_books(request):
    books = Book.objects.all()
    return render(request, 'view_books.html', {"books": books})

def search_book(request):
    query = request.GET.get("query")
    books = []
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(isbn__icontains=query)
        )
    return render(request, "search_book.html", {"books": books, "query": query})

def manage_users(request):
    return render(request, "manage_users.html")
