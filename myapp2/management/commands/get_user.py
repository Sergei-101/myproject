from django.core.management.base import BaseCommand
from myapp2.models import User
from random import randint

class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        user = User.objects.get(id=id)
        self.stdout.write(f'{user}')


