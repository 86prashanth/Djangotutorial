from django.contrib import admin
from dynamicapp.models import *
# Register your models here.
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display=('id','stuid')
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','stuid','stuname','stuemail','stupass')
    
admin.site.register(Student,StudentAdmin)