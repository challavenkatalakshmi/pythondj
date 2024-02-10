# Create your models here.
from django.db import models

class d(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # You should use hashed passwords in production
    address_line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    last_login = models.DateTimeField(auto_now=True)
    

    
