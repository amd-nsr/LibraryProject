from django.shortcuts import render
from catalog.models import Book, BookInstance, Author
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView

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

class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "templates/catalog/book_list.html"
    paginate_by = 4
    queryset = Book.objects.all()

    #def get_queryset(self):
    #   return Book.objects.filter(title__icontains='intro')[:5]

class BookDetailView(DetailView):
    model = Book
    #template_name = 'templates/catalog/book_detail.html'

class AuthorListView(ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'templates/catalog/author_list.html'
    queryset = Author.objects.all()
    paginate_by = 4

class AuthorDetailView(DetailView):
    model = Author
    #template_name = 'templates/catalog/author_detail.html'
