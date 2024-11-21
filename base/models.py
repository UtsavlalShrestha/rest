from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(null=True)
    username = models.CharField(max_length=300, unique=True)
    password = models.CharField(max_length=300)
    image = models.FileField()
    address = models.CharField(max_length=300)
    contact = models.CharField(max_length=300)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ProductType(models.Model):
    name = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=300)
    floor = models.CharField(max_length=300)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    stock = models.IntegerField()
    type = models.ForeignKey(ProductType,on_delete=models.SET_NULL, null =True)
    department = models.ManyToManyField(Department, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null =True)
    quantity = models.IntegerField()
    date = models.DateField()
    price = models.FloatField()
    vendor = models.ForeignKey('vendors', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

class Sell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null =True)
    quantity = models.IntegerField()
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customer_name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product

class vendors(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name