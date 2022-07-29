from django.contrib import admin

from shop.models import Product
from shop.models import Purchase


class PurchaseInline(admin.TabularInline):
    model = Purchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "color", "cost")
    search_fields = ("title",)
    inlines = [
        PurchaseInline,
    ]


# Register your models here.


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "count")
    list_filter = ("count",)
    search_fields = ("product__title",)

# Register your models here.
