from django.shortcuts import render, get_object_or_404
from catalog.models import Book, BookInstance, Author
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from catalog.forms import RenewBookForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    num_books = Book.objects.count()
    num_book_instances = BookInstance.objects.count()
    num_avilable_book_instances = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books' : num_books,
        'num_book_instances' : num_book_instances,
        'num_avilable_book_instances' : num_avilable_book_instances,
        'num_authors' : num_authors,
        'num_visits':num_visits,
    }
    return render(request, 'index.html', context=context)

class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "templates/catalog/book_list.html"
    paginate_by = 10
    queryset = Book.objects.all()

    #def get_queryset(self):
    #   return Book.objects.filter(title__icontains='intro')[:5]

class BookDetailView(DetailView):
    model = Book
    #template_name = 'templates/catalog/book_detail.html'

class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = "catalog/bookinstance_list_borrowed_user.html"
    paginate_by = 10
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status='o').order_by('due_back')

class AllBorrowedBooksListView(PermissionRequiredMixin, ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_librarians.html'
    paginate_by = 10
    permission_required = ("can_mark_returned")
    def get_queryset(self):
        return BookInstance.objects.filter(status='o').order_by('due_back')

class AuthorListView(ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'templates/catalog/author_list.html'
    queryset = Author.objects.all()
    paginate_by = 10

class AuthorDetailView(DetailView):
    model = Author
    #template_name = 'templates/catalog/author_detail.html'


def renew_book_librarian(self, pk):
    book_instance = get_object_or_404(BookInstance, pk)

    if request.method == "POST":
        form = RenewBookForm(request.POST)
        if form.is_valid:
            book_instance.due_back = form.cleaned_data['renewal_data']
            book_instance.save()
    else:
        proposed_renewal_date = datetime.date.today + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date':proposed_renewal_date})
    context ={
        'form':form,
        'book_instance':book_instance,
    }
    return render(request, 'catalog/book_renewal_librarian.html', context)

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial ={'date_of_death':'01/01/2019'}
class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class AuthorDelete(DetailView):
    model = Author
    success_url= reverse_lazy('authors')
