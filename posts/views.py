from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post


def index(request):
    if request.GET.get('title'):
        post_list = Post.objects.filter(title=request.GET.get('title'))
    elif request.GET.get('slug'):
        post_list = Post.objects.filter(slug=request.GET.get('slug'))
    else:
        post_list = Post.objects.all()
    return HttpResponse(",".join([x.title for x in post_list]))


def posts_author(request):
    posts_author_list = Post.objects.filter(user_id=request.user)
    return HttpResponse(",".join([x.title for x in posts_author_list]))
# Create your views here.
