from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='images/', default='accounts/static/image/user.jpg')
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
