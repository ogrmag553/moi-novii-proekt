from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)


class ServiceType(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    standard_time = models.CharField(max_length=30)
    price = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
class PartOrderltem(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    time = models.CharField(max_length=30)

    def __str__(self):
        return self.name
         