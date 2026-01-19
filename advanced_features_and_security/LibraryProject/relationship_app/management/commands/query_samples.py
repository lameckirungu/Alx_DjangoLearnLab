from django.core.management.base import BaseCommand, CommandParser
from relationship_app.models import Book

class Command(BaseCommand):
    help = "List books (Optional filters: --author, --library)"

    def add_arguments(self, parser):
        parser.add_argument('--author', type=str, help='Author name to filter by')
        parser.add_argument('--library', type=str, help='Library name to filter by')
        parser.add_argument('--json', action='store_true', help='Output JSON')

    def handle(self, *args, **options):
        qs = Book.objects.select_related('author').all()
        if options['author']:
            qs = qs.filter(author__name=options['author'])
        if options['library']:
            qs = qs.filter(library__name=options['library'])

        if options['json']:
            import json

            data  = [
                {"title": b.title, "author": b.author.name, "libraries": [l.name for l in b.library_set.all()]}
                for b in qs
            ]