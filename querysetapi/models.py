from django.db import models
import datetime
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField(unique=True,null=False)
    city=models.CharField(max_length=100)
    marks=models.IntegerField()
    pass_date=models.DateField()
    # adm_datetime=models.DateTimeField()
    # adm_datetime=models.DateTimeField()

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    empnum=models.IntegerField(unique=True,null=False)
    city=models.CharField(max_length=100)
    salary=models.IntegerField()
    join_date=models.DateField()
    
    

    