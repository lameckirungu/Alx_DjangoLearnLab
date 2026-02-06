from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class BookListView(generics.ListAPIView):
    """
    Retrieve a list of all books with support for filtering, searching and ordering.
    Allow read-only access to unauthenticated users.

    Use the following query parameters to filter by exact values:
    - `title`: Filter by book title.
    - `author`: Filter by author ID.
    - `publication_year`: Filter by exact year.
    *Example:* `/api/books/?publication_year=2020`

    Perform a case-insensitive partial search across multiple fields using the `search` parameter.
    - Fields: `title`, `author__name`.
    *Example:* `/api/books/?search=Harry`

    Sort the results by specifying a field name in the `ordering` parameter.
    - Supported Fields: `title`, `publication_year`.
    - Use a minus sign (`-`) for descending order.
    *Example:* `/api/books/?ordering=-publication_year`
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year'] # filter exact matches
    search_fields = ['title', 'author__name'] # searching (partial text matches)

    # Sorting/Ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] # default ordering


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