from django.urls import path, include
from . import views

# name parameter can be used to link pages: <a href="{% url 'index' %}">Home</a>
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookList.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetail.as_view(), name='book-detail'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetail.as_view(), name='author-detail'),
]