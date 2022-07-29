from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from django.db.models import Count, Sum, Max
import logging

logger = logging.getLogger(__name__)

logger.info("Informational message")


def shop(request):
    if request.GET.get('color'):
        products_list = Product.objects.filter(color=request.GET.get("color"))
    else:
        products_list = Product.objects.all()
    return HttpResponse(",".join([x.title for x in products_list]))


def filter_by_price(request):
    filtered_products = Product.objects.order_by('cost')
    return HttpResponse(",".join([x.title for x in filtered_products]))


