Detailed CRUD Operations and Documentation
------------------------------------------
CREATE:
-------
>>> from bookshelf.models import Book
>>> book = Book(title="1984", author="George Orwell", publication_year="1949")
>>> book.save()


>>> vars(book)
{'_state': <django.db.models.base.ModelState object at 0x784c97052fc0>, 'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': '1949'}

>>> Book.objects.all()
<QuerySet [<Book: Nineteen Eighty-Four>]>
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>