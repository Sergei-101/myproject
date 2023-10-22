from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    date_registration = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email},  phone: {self.phone}, address: {self.address}'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, default=777)
    def __str__(self):
        return self.name



class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_description = models.TextField()
    price_product = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_product = models.IntegerField()
    image = models.ImageField(upload_to='images')
    date_add_product = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'product_name: {self.product_name}, price_product: {self.price_product},'
                f'  quantity_product: {self.quantity_product}, image: {self.image}')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'customer: {self.customer}, products: {self.products},  date_ordered: {self.date_ordered}, total_price: {self.total_price}'


