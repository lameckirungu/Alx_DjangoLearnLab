DELETE
------
# commands
>>> from bookshelf.models import Book
>>> Book.objects.all()
<QuerySet [<Book: Nineteen Eighty-Four>]>
>>> Book.objects.all().delete()
(1, {'bookshelf.Book': 1})