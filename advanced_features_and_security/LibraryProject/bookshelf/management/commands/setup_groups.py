from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    """ 
    Management command to create user groups and assign permissions.

    Permissions defined on Book model:
    - can_view: Read-only access to books
    - can_create: Ability to create new books
    - can_edit: Ability to modify existing books
    - can_delete: Ability to remove 
    
    Groups created:
    - Viewers: can_view only
    - Editors: can_view, can_create, can_edit
    - Admins: can_view, can_create, can_edit, can_delete

    usage:
        python manage.py setup_groups
    """

    help = 'Create user groups and assign Book model permissions'

    def handle(self, *args, **options):
        # Get the Book mode's content type
        # ContentType is Django's way of linking permissions to specific models
        book_content_type = ContentType.objects.get_for_model(Book)
        