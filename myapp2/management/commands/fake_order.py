from django.core.management.base import BaseCommand
from myapp2.models import User, Product, Order
from random import randint

class Command(BaseCommand):
    help = "fake_order"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        test_list = ['Bob', 'Jon', 'Sam', 'Sergei', 'Ivan']
        for _ in range(count):
            user = User(name=test_list[randint(0, 4)], email=f'{randint(0, 100000)}@example.com',
                        password='secret',
                        phone=80295555555,
                        address='Minsk')
            user.save()

            test_list_1 = ['Milk', 'bacon', 'chicken', 'lamb', 'mutton']
            product = Product(product_name=test_list_1[randint(0, 4)], product_description='описание',
                              price_product=randint(1, 20),
                              quantity_product=randint(1, 5))
            product.save()

            order = Order(customer=user,total_price=product.price_product)
            order.save()
            order.products.add(product)


