from django.db import models

class Compani(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    actual_adres = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 

class Goods(models.Model):
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=30)
    brand = models.CharField(max_length=50)
    analogs = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
class Services(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.name