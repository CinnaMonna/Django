from django.core.management.base import BaseCommand, CommandParser
from typing import Any
from seminar_app.models import Author, Post

class Command(BaseCommand):
    help = 'Creates posts to fill db'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('count', type=int, help='Number of posts to create per author')

    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        count = kwargs['count']

        authors = Author.objects.all()

        for author in authors:
            for i in range(count):
                post = Post(
                    title=f'Title {i}',
                    content=f'Content {i}',
                    author=author
                )

                self.stdout.write(f'Created post {post}')
                post.save()
    