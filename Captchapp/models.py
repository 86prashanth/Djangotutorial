from django.db import models

# Create your models here.
class Student_captcha(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    
    def __str__(self):
        return str(self.id)