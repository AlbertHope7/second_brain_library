from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "subtitle", "author", "isbn"]
    list_filter = ["author"]
    order = ["-author"]
    search_fields = ["title", "author"]
