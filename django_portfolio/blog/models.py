
from django.db import models
from datetime import datetime


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateField(datetime.today())
