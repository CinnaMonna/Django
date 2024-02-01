from django.core.management.base import BaseCommand, CommandParser

from homework_app.models import Product, Order


class Command(BaseCommand):
    help = 'Adds products in order'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('order_id', type=int, help='Order id')
        parser.add_argument('product1_id', type=int, help='Product1 id')
        parser.add_argument('product2_id', type=int, help='Product2 id')
        
    def handle(self, *args, **kwargs) -> None:
        order_id = kwargs['order_id']
        product1_id = kwargs['product1_id']
        product2_id = kwargs['product2_id']

        order = Order.objects.get(id=order_id)
        product1 = Product.objects.get(id=product1_id)
        product2 = Product.objects.get(id=product2_id)

        order.products.add(product1, product2)
        self.stdout.write(f'Products {product1} and {product2} was added to order {order}')