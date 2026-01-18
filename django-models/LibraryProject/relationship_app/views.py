from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.contrib.auth.decorators import user_passes_test
from .models import Book, Library, UserProfile

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