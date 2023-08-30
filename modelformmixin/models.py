from django.db import models
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    
    # direct reverse
    # def get_absolute_url(self):
    #     return reverse("thanks")
    # direct fetch data
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    