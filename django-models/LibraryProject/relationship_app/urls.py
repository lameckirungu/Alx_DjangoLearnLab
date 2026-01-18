from django.urls import path
from .views import list_books, LibraryDetailView, LoginView, LogoutView, register

app_name = 'relationship_app' # namespace for reverse URL lookups

urlpatterns = [
    # Function-based view: /books
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('books/', list_books, name='list_books'),

    # class-based view: /library/<pk>
    path('/library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail')
]