from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    photo = models.ImageField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
