from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    subject1 = models.CharField(max_length=15)
    thgrade = models.CharField(max_length=10)
    prgrade = models.CharField(max_length=10)
def __str__(self):
    return self.name