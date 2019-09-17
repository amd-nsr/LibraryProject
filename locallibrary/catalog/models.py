import uuid
from datetime import date
from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    ISBN = models.CharField(max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField('Genre', help_text='Select a genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def get_abslute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class BookInstance(models.Model):
    LOAN_STATUS = (
        ('a', 'Avilable'),
        ('m', 'Maintenance'),
        ('r', 'Reserved'),
        ('o', 'On Loan'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    due_back = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, help_text='Avilablity')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=300, default="No IMPRINT")

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} {(self.book.title)}'

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField('Died', blank=True, null=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_abslute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name
