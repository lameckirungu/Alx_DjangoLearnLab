from django.db import models

class Author(models.Model):
    name = models.CharField(primary_key=True, max_length=100, null=False, blank=False)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(primary_key=True, max_length=100, blank=False)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)