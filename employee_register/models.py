from django.db import models

# Create your models here.

class Position(models.Model):
  title= models.CharField(max_length=50)

# email, mobile, telephone 
class Employee(models.Model):
		fullname = models.CharField(max_length=100)
		address = models.CharField(max_length=100)
		emp_code = models.CharField(max_length=3)
		email = models.EmailField(max_length=100)
		mobile = models.CharField(max_length=10)
		telephone = models.CharField(max_length=10)
		position = models.ForeignKey(Position, on_delete=models.CASCADE)