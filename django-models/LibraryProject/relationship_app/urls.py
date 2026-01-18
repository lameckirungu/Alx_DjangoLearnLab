from django.urls import path
from . import views

app_name = 'relationship_app' # namespace for reverse URL lookups

urlpatterns = [
    # Function-based view: /books
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('books/', views.list_books, name='list_books'),

    # class-based view: /library/<pk>
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail')
]