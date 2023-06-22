from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

# Create your views here.
class BookViewSet(viewsets.BookViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

