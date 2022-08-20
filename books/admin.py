from django.contrib import admin
from .models import Writer, Book, Comment, BooksLike


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ['name', 'user_author', 'datetime_created']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'user_author', 'status', 'price', 'datetime_created']
    list_filter = ['datetime_created']
    ordering = ['datetime_created']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'book', 'text_comment', 'datetime_created']
    list_filter = ['datetime_created']
    ordering = ['datetime_created']


@admin.register(BooksLike)
class BooksLikeAdmin(admin.ModelAdmin):
    list_display = ['username', 'book', 'datetime_created']
    list_filter = ['datetime_created']
    ordering = ['datetime_created']
