from django.db import models
from django.contrib.auth.models import User

class University(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=40)
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Faculty(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    course_teacher = models.CharField(max_length=255)

    def __str__(self):
        return self.name 
    
class Group(models.Model):
    name = models.CharField(max_length=50)
    number_of_students = models.CharField(max_length=50) 

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    academic_performance = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    assessments = models.ForeignKey(Assessments,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Items(models.Model):
    name = models.CharField(max_length=255)
    number_of_hours = models.IntegerField() 
    
