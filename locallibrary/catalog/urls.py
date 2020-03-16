from django.urls import path
from catalog import views
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books-list'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors-list'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed-books', views.AllBorrowedBooksListView.as_view(), name='borrowed-books' ),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew_book_librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),

]
