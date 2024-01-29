from django.core.management.base import BaseCommand, CommandParser
import datetime

from homework_app.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Creates fake orders to fill DB'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('count', type=int, help='Number of order of each client')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        clients = Client.objects.all()
        products = Product.objects.all()

        for client in clients:
            for i in range(count):
                order = Order(
                    client=client,
                    product=products[i],
                    order_sum=35.50 + i
                )

                self.stdout.write(f'Order {order} was created')
                order.save()
    
