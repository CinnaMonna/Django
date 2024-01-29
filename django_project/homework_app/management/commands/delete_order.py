from django.core.management.base import BaseCommand, CommandParser
from homework_app.models import Order

class Command(BaseCommand):
    help = 'Deletes an order by id'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('id', type=int, help='Order id to delete')

    def handle(self, *args, **kwargs):
        id = kwargs['id']

        order = Order.objects.filter(pk=id).first()

        order.delete()
        self.stdout.write(f'Deleted order: {order}')
 