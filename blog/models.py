from django.db import models
from profiles.models import UserProfile


# Model for blog post section in admin

class Blog(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        'profiles.UserProfile', max_length=40,
        null=True, blank=True, on_delete=models.PROTECT)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
