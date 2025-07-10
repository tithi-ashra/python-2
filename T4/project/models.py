from django.db import models

# Create your models here.
class Student(models.Model):
    StuID = models.IntegerField()
    Name = models.CharField(max_length=70)
    Email = models.EmailField(max_length=70)
    Result = models.CharField(max_length=15)
    