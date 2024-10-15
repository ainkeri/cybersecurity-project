from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=50, default=None)
    content = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)