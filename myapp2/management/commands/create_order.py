from django.core.management.base import BaseCommand
from myapp2.models import User, Order, Product
from random import randint, choice

class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument("User_id", type=int, help="User ID")
        parser.add_argument("Count", type=int, help="Count")


    def handle(self, *args, **kwargs):
        User_id = kwargs.get('User_id')
        count = kwargs.get('Count')

        Product_id = Product.objects.values_list('id', flat=True)

        user = User.objects.filter(pk=User_id).first()

        order = Order(customer=user)
        total_price = 0
        for i in range(count):
            product = Product.objects.filter(pk=choice(Product_id)).first()
            total_price += float(product.price_product)
            order.total_price = total_price
            order.save()
            order.products.add(product)



