from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogposts")
