from django.contrib import admin

from library.models import Author, Book, Category, Publisher

# Register your models here.
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
