from .serializers import BookSerializer
from .models import Book
from rest_framework import generics
from rest_framework import viewsets

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    Book Viewset for handling CRUD operations
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer