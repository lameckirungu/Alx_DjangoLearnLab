from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class BookListView(generics.ListAPIView):
    """
    Retrieve all books (GET)
    Allow read-only access to unauthenticated users.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID (GET)
    Allow read-only access to unauthenticated users.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    """
    Create a new book (POST)
    REstrict to authenticated users only
    """
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        """Custom behavior during creation"""
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    Modify an existing book (PUT/PATCH)
    Restrict to authenticated users only.
    """
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(generics.DestroyAPIView):
    """
    Remove a book (DELETE)
    Restrict to authenticated users only.
    """
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer