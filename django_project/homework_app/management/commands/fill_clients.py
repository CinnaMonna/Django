from django.core.management.base import BaseCommand, CommandParser
import datetime

from homework_app.models import Client


class Command(BaseCommand):
    help = 'Creates fake clients to fill DB'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('count', type=int, help='Number of clients')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(1, count + 1):
            client = Client(
                name=f'Client{i}',
                email=f'client{i}@bk.ru',
                phone=f'+7*****{i}',
                adress=f'adress{i}',
                )
            
            self.stdout.write(f'Client {client} was created')
            client.save()


