from django.forms import ModelForm
from .models import Book, Writer, Comment, BooksLike


class NewBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'content', 'author', 'price', 'status', 'cover', ]


class NewWriterForm(ModelForm):
    class Meta:
        model = Writer
        fields = ['name', 'content']


class NewCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text_comment', 'recommend']


class NewBooksLikeForm(ModelForm):
    class Meta:
        model = BooksLike
        fields = ['book']
