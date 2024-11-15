from django.db import models

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()

    def __str__(self):
        return self.name

class ProductTable(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    stock = models.IntegerField()
    type = models.ForeignKey(ProductType)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class PurchaseTable(models.Model):
    product = models.ForeignKey(ProductTable)
    quantity = models.IntegerField()
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.ForeignKey(vendor, on_delete=models.SET_NULL)

    def __str__(self):
        return self.product

class SalesTable(models.Model):
    product = models.ForeignKey(ProductTable)
    quantity = models.IntegerField()
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customer_name = models.CharField(max_length=50)


    def __str__(self):
        return self.product

class vendor(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return self.name