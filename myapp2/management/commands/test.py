from django.core.management.base import BaseCommand
from myapp2.models import User, Product
from random import randint

class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **kwargs):
        prduct_id = Product.objects.values_list('id', flat=True)
        self.stdout.write(f'{prduct_id}')


