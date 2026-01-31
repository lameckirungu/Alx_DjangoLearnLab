from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

# Router URLs for BookViewSet
router = DefaultRouter()
router.register('books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList View
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls))
]