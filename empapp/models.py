from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    salary=models.PositiveIntegerField()
    contact=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
