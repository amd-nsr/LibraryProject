from django.contrib import admin
from .models import Book, BookInstance, Author, Genre, Language

 
class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'language')
    inlines = [BookInstanceInline]
    
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status',)
    list_filter = ('status', 'due_back')
    fieldsets = (
        ('Book Info',{
            'fields':('book', 'id')
            }),
        ('Avilability',{'fields':('status', 'due_back'),
                        }),
                )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    
admin.site.register(Genre)
admin.site.register(Language)
