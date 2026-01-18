from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .models import Book, Library, Author

# Function-based view: list all books
def list_books(request):
    """
    Display all books in the database.

    request: HttpRequest object from Django
    returns: HttpResponse with rendered list_books.html template
    """
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """
    Display a specific library and all its books.

    model: the model this view queries (Library)
    template_name: path to the template to render
    context_object_name: name of the variable passed to template (library)
    """

    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class LoginView(DjangoLoginView):
    """  
    Django's built-in LoginView handles user authentication.
    Renders the login template and processes login form submissions.
    """
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True

class LogoutView(DjangoLogoutView):
    """
    Django's built-in LogoutView handles user logout.
    Clears the session and redirects to home.
    """
    template_name = 'relationship_app/logout.html'
    next_page = 'relationship_app:login'

def register(request):
    """
    Handle user registration with UserCreationFrom

    GET: Display registration form
    POST: Process form submission and create new user
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # create user in db
            login(request, user)
            return redirect('relationship_app:list_books') # Redirect to home page
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})

# Helper functions to check roles
def is_admin(user):
    return user.userprofile.role == 'Admin'
def is_librarian(user):
    return user.userprofile.role == 'Librarian'
def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    """View only accessible to Admin users"""
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    """View only accessible to Librarian users"""
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    """View only accessible to Member users"""
    return render(request, 'relationship_app/member_view.html')

# Permission-based views for Book management
@permission_required('relationship_app.can_add_book')
def add_book(request):
    """View to add a new book - requires can_add_book permission"""
    if request.method == 'POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author')
        try:
            author = Author.objects.get(name=author_name)
            Book.objects.create(title=title, author=author)
            return redirect('relationship_app:list_books')
        except Author.DoesNotExist:
            return render(request, 'relationship_app/add_book.html', {'error': 'Author not found'})
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    """View to edit an existing book - requires can_change_book permission"""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title', book.title)
        book.save()
        return redirect('relationship_app:list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    """View to delete a book - requires can_delete_book permission"""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('relationship_app:list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})