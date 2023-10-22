from django.shortcuts import render
import datetime
import logging
from myapp3.forms import UserForm, ManyFieldsForm, ImageForm, UpdateProduct, AddProduct
from myapp2.models import Product
from .models import User
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
        return render(request, 'myapp3/form.html', {'form': form})

def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            # Делаем что-то с данными
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsForm()
    return render(request, 'myapp3/form.html', {'form': form})

def many_fields_form_widjet(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            # Делаем что-то с данными
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsForm()
    return render(request, 'myapp3/form.html', {'form': form})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'myapp3/form.html', {'form':form, 'message': message})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp3/form.html', {'form':form})

def update_product(request):
    if request.method == 'POST':
        form = UpdateProduct(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            id_product = form.cleaned_data['id_product']
            product_name = form.cleaned_data['product_name']
            quantity = form.cleaned_data['quantity']
            logger.info(f'Получили {id_product=}, {product_name=}, {quantity=}.')
            product = Product.objects.filter(pk=id_product).first()
            product.quantity_product = quantity
            product.product_name = product_name
            product.save()
            message = f'Название продукта  изменено на {product_name} кол-во = {quantity}'
    else:
        form = UpdateProduct()
        message = 'Заполните форму'
    return render(request, 'myapp3/form.html', {'form':form, 'message': message})


def add_product(request):
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            product_description = form.cleaned_data['product_description']
            price_product = form.cleaned_data['price_product']
            quantity_product = form.cleaned_data['quantity_product']
            images = form.cleaned_data['images']
            fs = FileSystemStorage()
            fs.save(images.name, images)
            logger.info(f'Получили {product_name=}, {product_description=}, {price_product=}, {quantity_product}.')
            product = Product(product_name=product_name, product_description=product_description,
                              price_product=price_product, quantity_product=quantity_product, image=images.name)
            product.save()

            message = f'Название продукта  {product_name} кол-во = {quantity_product}'
    else:
        form = AddProduct()
        message = 'Заполните форму'
    return render(request, 'myapp3/form.html', {'form':form, 'message': message})