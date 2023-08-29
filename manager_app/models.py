from django.db import models
from manager_app.managers import Custommanager

# Create your models here.
class Manager_student(models.Model):
    name = models.CharField(max_length=200)
    roll=models.IntegerField()
    objects=models.Manager()
    students=Custommanager()
    
class Proxystudent(Manager_student):
    students=Custommanager()
    class Meta:
        proxy=True 
        ordering=['name']