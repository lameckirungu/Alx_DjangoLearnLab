from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Author, Book, Library, Librarian

# Function-based view: list all books
def list_books(request):
    """
    Display all books in the database.

    request: HttpRequest object from Django
    returns: HttpResponse with rendered list_books.html template
    """
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """
    Display a specific library and all its books.

    model: the model this view queries (Library)
    template_name: path to the template to render
    context_object_name: name of the variable passed to template (library)
    """

    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'