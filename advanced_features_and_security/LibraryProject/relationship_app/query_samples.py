import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author"""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author}:")

        for b in books:
         print(f"- {b.title} - {b.author.name}")
        
    except Author.DoesNotExist:
        print(f"No Author found with name '{author_name}'")
    

def list_books_in_library(library_name):
    """List all books in a library"""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()

        print(f"Books in {library_name}:")
        for b in books:
            print(f"- {b.title} - {b.author}")

    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")

def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    try:
        library = Library.objects.get(library=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian {library_name} belongs to the library {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for '{library_name}'")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")
if __name__ == "__main__":
    # Example usage
    query_books_by_author("Chinua Achebe")
    list_books_in_library("Nairobi Central Library")
    retrieve_librarian_for_library("Nairobi Central Library")
