from django.shortcuts import render
from catalog.models import Book, BookInstance, Author

def index(request):
    num_books = Book.objects.count()
    num_book_instances = BookInstance.objects.count()
    num_avilable_book_instances = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    
    context = {
        'num_books' : num_books,
        'num_book_instances' : num_book_instances,
        'num_avilable_book_instances' : num_avilable_book_instances,
        'num_authors' : num_authors,
    }
    return render(request, 'index.html', context=context)
