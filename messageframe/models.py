from django.db import models

# Create your models here.
class Messagesframe(models.Model):
    name = models.CharField(max_length=10)
    email= models.EmailField(max_length=25)
    password = models.CharField(max_length=10)
    