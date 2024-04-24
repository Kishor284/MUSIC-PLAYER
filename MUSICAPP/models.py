from django.db import models

# Create your models here.
class signup(models.Model):
    Email=models.CharField(max_length=50)
    Name=models.CharField(max_length=50)
    Username=models.CharField(max_length=50)
    Phoneno=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)