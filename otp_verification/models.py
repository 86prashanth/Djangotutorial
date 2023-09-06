from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,
from django.contrib.auth.models import AbstractUser
# from otp_verification.managers import UserManager
# from phonenumber_field.modelfields import PhoneNumberField
import random

# class JobUser(AbstractBaseUser):
#     VERIFICATION_TYPE = [
#         ('sms','SMS'),
#     ]
    
#     phone_number = PhoneNumberField(unique = True)
#     verification_method = models.CharField(max_length=10,choices= VERIFICATION_TYPE)
#     is_active = models.BooleanField(default= True)
#     is_admin = models.BooleanField(default= False)
#     is_staff = models.BooleanField(default= False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = "phone_number"
#     objects = UserManager()
    
#     def __str__(self):
#         return str(self.phone_number)
    
#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return self.is_admin
    
class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=12)
    
class Code(models.Model):
    number=models.CharField(max_length=5,blank=True)
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.number)
    
    def save(self,*args,**kwargs):
        number_list=[x for x in range(10)]
        code_items=[]
        for i in range(5):
            num=random.choice(number_list)
            code_items.append(num)
        code_string="".join(str(item) for item in code_items)
        self.number=code_string
        super().save(*args,**kwargs)