from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Book

# On the top lines we’ve imported ListView and our Book model. Then we create a BookListView
# class that specifies the model to use and the template (not created yet).
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'