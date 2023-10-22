from django.urls import path

from .views import my_view,all_orders,all_orders_sorted

urlpatterns = [
 path('', my_view, name='index'),
 path('all_orders/<int:user_id>/', all_orders, name='all_orders'),
 path('all_orders_sorted/<int:user_id>/<int:days_ago>/', all_orders_sorted, name='all_orders_sorted'),
]