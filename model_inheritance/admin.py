from django.contrib import admin
from model_inheritance.models import *
# Register your models here.
# @admin.register(CommonInfo)
# class CommonInfoAdmin(admin.ModelAdmin):
#     list_display=['name','age','date']
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','age','date','fees']
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','age','date','salary']
    
@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display=['id','name','age','date','payment']
    
@admin.register(Examcenter)
class ExamcenterAdmin(admin.ModelAdmin):
    list_display=['id','cname','city']
    
@admin.register(MyExamcenter)
class ExamcenterAdmin(admin.ModelAdmin):
    list_display=['id','cname','city']
    
@admin.register(Studentcenter)
class StudentcenterAdmin(admin.ModelAdmin):
    list_display=['id','cname','city','name','roll']
    


