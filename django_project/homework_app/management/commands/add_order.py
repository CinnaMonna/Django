from django.core.management.base import BaseCommand, CommandParser

from homework_app.models import Client, Order


class Command(BaseCommand):
    help = 'Creates order'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('client_id', type=int, help='Client id')

    def handle(self, *args, **kwargs) -> None:
        client_id = kwargs['client_id']
        client = Client.objects.get(id=client_id)

        # products_in_order = Products_in_order.objects.filter(order_id=order_id)
        # summary_cost = 0
        # for product in products_in_order:
        #     summary_cost += product.cost

        order = Order(
            client=client
        )

        order.save()
        self.stdout.write(f'Order {order} was created')
        