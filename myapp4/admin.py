from django.contrib import admin
from myapp2.models import User, Product, Order, Category

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'total_price']
    ordering = ['-date_ordered']



class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address']
    search_fields = ['name']
    search_help_text = 'Поиск по Имени (name)'


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['product_name', 'category', 'quantity_product']

    """Отдельный продукт."""

    readonly_fields = ['date_add_product']
    fieldsets = [
    (
        None,
        {
            'classes': ['wide'],
            'fields': ['product_name'],
        },
    ),
    (
        'Подробности',
        {
            'classes': ['collapse'],
            'description': 'Категория товара и его подробное описание',
            'fields':['category', 'product_description'],
    },
    ),
    (
        'Бухгалтерия',
        {
            'fields': ['price_product', 'quantity_product'],

        }
    ),
  ]



admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)





