CREATE:
-------
# Commands
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year="1949")
# Expected Output
>>> Book.objects.all()
<QuerySet [<Book: 1984>]>