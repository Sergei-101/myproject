from django.core.management.base import BaseCommand
from myapp2.models import Product
from random import randint

class Command(BaseCommand):
    help = "Update user name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('product_name', type=str, help='product_name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product_name = kwargs.get('product_name')
        product = Product.objects.filter(pk=pk).first()
        product.product_name = product_name
        product.save()
        self.stdout.write(f'{product_name}')



