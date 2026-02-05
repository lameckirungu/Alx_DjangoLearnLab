from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book modle
    serializers all fields: title, publication_year, and author.
    Includes custom validation to ensure publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

        # Custom validation for public year
        def validate_publication_year(self, value):
            current_year = date.today().year
            if value > current_year:
                raise serializers.ValidationError("The publication year cannot be in the future.")
            return value
        
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author Model.
    Includes the author's name and a nested BookSerializer that
    dynamically serializers all books related to the author (one-to-one relationship).
    The 'books' field uses teh `related_name` defined on the Book.author FK.
    """
    books = BookSerializer(many=True, read_only=True, source='book_set')

    class Meta:
        model = Author
        fields = ['name', 'books']
        