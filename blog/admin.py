from django.contrib import admin
from .models import Post


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'author',
        'image',
        'content',
        'created_on',
    )


admin.site.register(Post, BlogAdmin)
