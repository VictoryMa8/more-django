from django.urls import path, include
from . import views

# name parameter can be used to link pages: <a href="{% url 'index' %}">Home</a>
urlpatterns = [
    path('', views.index, name='index')
]