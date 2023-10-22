from datetime import datetime, timedelta, date

from django.shortcuts import render, get_object_or_404
from .models import User, Product, Order


def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp2/index.html", context)


def all_orders(request, user_id):
    products = []
    user = User.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(customer=user).all()
    for order in orders:
        products.append(order.products.all())

    return render(request, 'myapp2/all_orders.html', {'user': user, 'orders': orders, 'products': products})

def all_orders_sorted(request, user_id, days_ago):
    products = []
    product_list = []
    now = date.today()
    before = now - timedelta(days=days_ago)
    user = User.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(customer=user, date_ordered__range=(before, now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in product_list:
                product_list.append(product)

    return render(request, 'myapp2/all_orders_sorted.html', {'user': user,
                                                             'product_list': product_list, 'days': days_ago})