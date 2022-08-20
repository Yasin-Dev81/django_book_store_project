from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=False)
    # date
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_edited = models.DateTimeField(auto_now=True)
    # status: available, unavailable
    STATUS_CHOICES = (('ava', 'Available'), ('una', 'Unavailable'))
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    # author with fk
    # author = models.CharField(max_length=200, null=False, blank=False)
    author = models.ForeignKey('Writer', on_delete=models.CASCADE)
    user_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # cover
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return "(%s) from (%s) is %s$" % (self.title, self.author, self.price)

    def get_absolute_url(self):
        return reverse('book_detail_url', args=[self.id, self.title, ])


class Writer(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=True, blank=True)

    user_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # date
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('writer_detail_url', args=[self.id, ])


class Comment(models.Model):
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='comments')

    text_comment = models.TextField(blank=False, null=False)

    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True)

    # date
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[%s in %s]: %s' % (self.username, self.book.title, self.text_comment, )

    def get_absolute_url(self):
        return reverse('book_detail_url', args=[self.book.id, self.book.title])


class BooksLike(models.Model):
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='book_like')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='book_like')

    # date
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[%s]: %s' % (self.username, self.book.id, )

    def get_absolute_url(self):
        return reverse('book_detail_url', args=[self.book.id, self.book.title])
