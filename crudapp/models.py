from django.db import models

# Create your models here.
class Crudapp(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

class User(models.Model):
    student_name=models.CharField(max_length=100)
    teacher_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.student_name