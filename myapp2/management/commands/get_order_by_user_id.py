from django.core.management.base import BaseCommand
from myapp2.models import User, Product, Order
from random import randint

class Command(BaseCommand):
    help = "Get all order by user id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            order = Order.objects.filter(customer=user)
            intro = f'{user.name} заказал, {order}\n'
            self.stdout.write(f'{intro}')




