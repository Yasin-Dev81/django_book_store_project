from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .models import Book, Writer, BooksLike, Comment
from .forms import NewCommentForm


# finished
class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'


# finished
def book_detail_view(request, pk, title):
    str(title).replace('-', ' ')
    # get book object
    try:
        book = get_object_or_404(Book, pk=pk, title=title)
    except MultipleObjectsReturned:
        book = Book.objects.filter(pk=pk, title=title).first()
    # comment
    if request.method == "GET":
        # get book comment & comment form
        comments = book.comments.all()
        comment_form = NewCommentForm()
        get_context = {
            'book': book,
            'comments': comments,
            'form': comment_form,
            'like_count': book.book_like.count(),
            'liked_user': (len(book.book_like.filter(username=request.user)) > 0) if request.user.is_authenticated else None,
        }
        return render(request, 'books/book_detail.html', context=get_context)
    elif request.method == "POST":
        new_comment_form = NewCommentForm(request.POST)
        if new_comment_form.is_valid():
            new_comment = new_comment_form.save(commit=False)  # save data
            new_comment.book = book
            new_comment.username = request.user
            new_comment.save()
            return redirect(reverse('book_detail_url', args=[pk, title]))
        else:
            comment_form = NewCommentForm()
            return render(request, "books/book_detail.html", context={'form': comment_form})


# finished
def writer_list_view(request):
    writer_list = Writer.objects.all()
    page = request.GET.get('page', 1)

    paginate_by = 4
    paginator = Paginator(writer_list, paginate_by)

    try:
        writers = paginator.page(page)
    except PageNotAnInteger:
        writers = paginator.page(1)
    except EmptyPage:
        writers = paginator.page(paginator.num_pages)

    return render(request, 'books/writer_list.html', context={'writers': writers})


# finished
def writer_detail_view(request, pk):
    writer = get_object_or_404(Writer, pk=pk)
    return render(request, 'books/writer_detail.html', context={'writer': writer})


# finished
class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Book
    fields = ['title', 'content', 'author', 'price', 'status', 'cover']
    template_name = 'books/create_book.html'

    def test_func(self):
        return self.request.user.is_staff


# finished
class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    fields = ['title', 'content', 'price', 'status', 'cover']
    template_name = 'books/update_book.html'

    def test_func(self):
        return self.get_object().user == self.request.user or self.request.user.is_superuser


# finished
class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    success_url = reverse_lazy('home_url')
    template_name = 'books/delete_book.html'

    def test_func(self):
        return self.get_object().user == self.request.user or self.request.user.is_superuser


# finished
class WriterCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Writer
    fields = ['name', 'content']
    template_name = 'books/create_writer.html'

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


# finished
class WriterUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Writer
    fields = ['name', 'content']
    template_name = 'books/update_writer.html'

    def test_func(self):
        return self.get_object().user == self.request.user or self.request.user.is_superuser


# finished
@login_required()
def book_like_view(request, pk, like_type: str):
    if like_type == 'like':
        liked_book = get_object_or_404(Book, pk=pk)
        BooksLike.objects.create(username=request.user, book=liked_book).save()
        return redirect(reverse('book_detail_url', args=(pk, liked_book.title)))
    elif like_type == 'unlike':
        liked_book = get_object_or_404(Book, pk=pk)
        BooksLike.objects.get(username=request.user, book=liked_book).delete()
        return redirect(reverse('book_detail_url', args=(pk, liked_book.title)))


# finished
@login_required()
def inactive_comment_view(request, pk):
    if request.user.is_staff:
        comment = get_object_or_404(Comment, pk=pk)
        comment.is_active = False
        comment.save()
        return redirect(reverse('book_detail_url', args=(comment.book.pk, comment.book.title)))
    else:
        return HttpResponse('Access is limited')
