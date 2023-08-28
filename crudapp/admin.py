from django.contrib import admin
from crudapp.models import Crudapp,User
# Register your models here.
@admin.register(Crudapp)
class CrudAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password']
    
@admin.register(User)
class CrudAdmin(admin.ModelAdmin):
    list_display=['teacher_name','student_name','email','password']

