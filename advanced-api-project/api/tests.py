from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    """
    Test suite for the Book API endpoints including CRUD,
    permissions, and filtering functionality.
    """
    def setUp(self):
        """
        Set up initial data for testing. Creates a user, an author,
        and a book to be used i varioius test cases.
        """
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.author = Author.objects.create(name="Timubuktu")
        self.book = Book.objects.create(
            title="You and Me",
            publication_year=2002,
            author=self.author
        )

        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})

    def test_create_book_authenticated(self):
        """  
        Ensure the authenticated user can create a new book.
        Verifies status code 201 and data integrity
        """
        self.client.login(username='testuser', password='password123')
        data = {
            "title": "In the Shadows",
            "publication_year": 1937,
            "author": self.author.pk
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
    
    def test_create_book_unauthenticated(self):
        """  
        Ensure unauthenticated users are blocked from creating books.
        Expects a 403 Forbidden status.
        """
        data = {"title": "Anonymous Book", "publication_year": 2020, "author": self.author.pk}
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_update_book(self):
        """Verify that an authenticated user can update an existing book's title"""
        self.client.login(username='testuser', password='password123')
        data = {
            "title": "You and Me updated",
            "publication_year": 2002,
            "author": self.author.pk
        }

        response = self.client.put(reverse('book-update', kwargs={'pk': self.book.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "You and Me updated")

    def test_delete_book(self):
        """
        Confirm that an authenticated user can delete a book entry.
        """
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_by_title(self):
        """
        Test the filtering backend by searching for a specific title.
        """
        response = self.client.get(f"{self.list_url}?title=You and Me")
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], "You and Me")