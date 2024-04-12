from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()  
    email=models.EmailField(max_length=100)
    address=models.TextField()
    image=models.ImageField(upload_to='images/')
    file=models.FileField(upload_to='files/')

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to='images/') 