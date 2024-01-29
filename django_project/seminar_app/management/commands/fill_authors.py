from django.core.management.base import BaseCommand
import datetime
from typing import Any

from seminar_app.models import Author

class Command(BaseCommand):
    help = 'Creates new users'

    def handle(self, *args: Any, **options: Any) -> str | None:
        for i in range(1, 11):
            author = Author(
                name=f'Author {i}',
                last_name=f'Last Name {i}',
                email=f'mail{i}@example.com',
                bio='Something',
                birthday=datetime.date(2000, 1, 1)
                )
            self.stdout.write(f'Author {author} created')
            author.save()
             