from django.core.management.base import BaseCommand, CommandParser
from seminar_app.models import Author

class Command(BaseCommand):
    help = 'Deletes an author by id'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('id', type=int, help='Author id to delete')

    def handle(self, *args, **kwargs):
        id = kwargs['id']

        author = Author.objects.filter(pk=id).first()

        author.delete()
        self.stdout.write(f'Deleted author: {author}')
 