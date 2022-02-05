from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return self.username


class Bookmark(models.Model):

    title = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(to=User, on_delete=models.PROTECT)
    private = models.BooleanField(default=True)
