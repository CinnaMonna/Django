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
                    content=f'Text {i}: Sed ut perspiciatis, qui in ea voluptate velit esse,' 
                    f'quam nihil molestiae consequatur, vel illum, quae ab illo inventore' 
                    f'veritatis et quasi architecto beatae vitae dicta sunt, explicabo.'
                    f'Sed ut perspiciatis, quia voluptas sit, aspernatur aut odit aut fugit,'
                    f'sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt',
                    author=author
                )

                self.stdout.write(f'Created post {post}')
                post.save()
    