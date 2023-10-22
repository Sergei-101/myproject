from django.core.management.base import BaseCommand
from myapp2.models import User
from random import randint

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        test_list = ['Bob', 'Jon', 'Sam', 'Sergei','Ivan']
        for i in range(5):
            user = User(name=test_list[i], email=test_list[i] + '@example.com',
                        password=test_list[i] + 'secret',
                        phone=80295555555,
                        address='Minsk')
            user.save()
            self.stdout.write(f'{user}')


