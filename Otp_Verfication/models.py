from django.db import models
from django.contrib.auth.models import AbstractUser
from Otp_Verfication.manager import UserManager
# Create your models here.

class User(AbstractUser):
    phone_number=models.CharField(max_length=12,unique=True)
    is_phone_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=100)
    
    
    
    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]
    objects=UserManager()
    
    