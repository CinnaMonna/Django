from django.core.management.base import BaseCommand, CommandParser

from homework_app.models import Client, Product, Order, Products_in_order

class Command(BaseCommand):
    help = 'Count and set summary cost of order'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('order_id', type=int, help='Order id')

    def handle(self, *args, **kwargs) -> None:
        order_id = kwargs['order_id']
        order = Order.objects.get(id=order_id)
        client = Client.objects.get(id=order.client_id)

        products_in_order = Products_in_order.objects.filter(order_id=order_id)
        summary_cost = 0
        for product in products_in_order:
            summary_cost += product.cost

        order = Order(
            client=client,
            summary_cost=summary_cost
        )
        
        order.save()
        self.stdout.write(f'summary cost of order {order} was added')
        