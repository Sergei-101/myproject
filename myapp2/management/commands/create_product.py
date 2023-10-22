from django.core.management.base import BaseCommand
from myapp2.models import Product
from random import randint

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        test_list = ['Milk', 'bacon', 'chicken', 'lamb','mutton']
        for i in range(5):
            product = Product(product_name=test_list[i], product_description=test_list[i] + 'описание',
                        price_product=randint(1,20),
                        quantity_product=randint(1,5))
            product.save()
            self.stdout.write(f'{product}')


        