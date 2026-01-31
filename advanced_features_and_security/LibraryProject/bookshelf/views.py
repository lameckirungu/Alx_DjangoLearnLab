from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    return render(request, book_id)

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    return render(request, book_id)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request, book_id):
    return render(request, book_id)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    return render(request, book_id)