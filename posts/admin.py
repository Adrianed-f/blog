from django.contrib import admin

from posts.models import Post
from posts.models import Tag


@admin.register(Post)
class PostUser(admin.ModelAdmin):
    list_display = ("user", "title", "slug", "created_at")
    fields = ("user", "title", "slug", "text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "slug", "text")
    raw_id_fields = ("user",)


# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("title",)
