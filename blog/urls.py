"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from posts.views import index
from profiles.views import profiles
from profiles.views import profiles_post
from shop.views import shop
from shop.views import filter_by_price
# from shop.views import filter_by_cost_purchase
# from shop.views import filter_by_purchases
from posts.views import posts_author

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('profiles/', profiles, name='profiles'),
    path('profiles/posts/', profiles_post, name='profiles_post'),
    path('shop/', shop, name='shop'),
    path('posts/author/', posts_author, name='posts_author'),
    path('filter/cost/', filter_by_price, name='filter_by_price'),
    # path('filter/cost/purchase/', filter_by_cost_purchase, name='filter_by_cost_purchase'),
    # path('filter/purchases/', filter_by_purchases, name='filter_by_purchases')


]

