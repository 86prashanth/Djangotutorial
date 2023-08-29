from django.db import models

# Create your models here.
# abstract
class CommonInfo(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    date=models.DateField()
    class Meta:
        abstract=True
        
        
# class Student(models.Model):
class Student(CommonInfo):
    # name=models.CharField(max_length=100)
    # age=models.IntegerField()
    fees=models.IntegerField()
    date=None


# class Teacher(models.Model):
class Teacher(CommonInfo):
    # name=models.CharField(max_length=100)
    # age=models.IntegerField()
    # date=models.DateField()
    salary=models.IntegerField()
    
# class Contractor(models.Model):
class Contractor(CommonInfo):
    # name=models.CharField(max_length=100)
    # age=models.IntegerField()
    date=models.DateTimeField()
    payment=models.IntegerField()
    
# Model inheritance
class Examcenter(models.Model):
    cname=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    
class Studentcenter(Examcenter):
    name=models.CharField(max_length=70)
    roll=models.IntegerField()
    
# proxy model 
class MyExamcenter(Examcenter):
    class Meta:
        proxy=True
        # ordering=['id']
        ordering=['city']