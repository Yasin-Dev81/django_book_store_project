from django.urls import path
from . import views


urlpatterns = [
    path('book-list/', views.BookListView.as_view(), name='book_list_url'),
    path('book-detail/<int:pk>/<str:title>/', views.book_detail_view, name='book_detail_url'),
    path('writer-list/', views.writer_list_view, name='writer_list_url'),
    path('book-detail/<int:pk>/', views.writer_detail_view, name='writer_detail_url'),
    path('create-book/', views.BookCreateView.as_view(), name='create_book_url'),
    path('update-book/<int:pk>/', views.BookUpdateView.as_view(), name='update_book_url'),
    path('delete-book/<int:pk>/', views.BookDeleteView.as_view(), name='delete_book_url'),
    path('create-writer/', views.WriterCreateView.as_view(), name='create_writer_url'),
    path('update-writer/<int:pk>/', views.WriterUpdateView.as_view(), name='update_writer_url'),
    path('book-like/<int:pk>/<str:like_type>', views.book_like_view, name='book_like_url'),
    path('inactive-comment/<int:pk>/', views.inactive_comment_view, name='inactive_comment_url'),
]
