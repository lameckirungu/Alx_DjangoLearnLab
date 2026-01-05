DELETE
------
>>> Book.objects.all()
<QuerySet [<Book: Nineteen Eighty-Four>]>
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>