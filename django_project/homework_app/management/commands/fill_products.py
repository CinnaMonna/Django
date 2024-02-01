from django.core.management.base import BaseCommand, CommandParser

from homework_app.models import Product
from random import randint


class Command(BaseCommand):
    help = 'Creates fake products to fill DB'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('count', type=int, help='Number of products')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(1, count + 1):
            product = Product(
                title=f'Product{i}',
                description=f'description{i}',
                price=randint(10,50)*1.1,
                count=randint(1,10),
                )
            
            self.stdout.write(f'Product {product} was created')
            product.save()



