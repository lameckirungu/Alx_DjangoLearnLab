from .serializers import BookSerializer
from .models import Book
from rest_framework.generics import ListAPIView

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer