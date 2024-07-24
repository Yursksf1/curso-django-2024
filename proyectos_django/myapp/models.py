from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    

class Product(models.Model):
    product_name = models.CharField(max_length=80)
    brand = models.CharField(max_length=80)
    description = models.TextField() #large texts
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    stock = models.IntegerField()
    
    def __str__(self):
        return f"{self.product_name}"
# referencia para crear modelos: 
# https://docs.djangoproject.com/en/5.0/ref/models/fields
# https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.IntegerField

# Producto 
# -- nombre del producto
# -- valor de compra
# -- valor de venta 