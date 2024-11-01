from django.contrib import admin
from .models import Book, Order

class BookModelAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish_date", "publisher")
    search_fields = ('title', 'author', 'publisher')
admin.site.register(Book, BookModelAdmin) 
admin.site.register(Order)