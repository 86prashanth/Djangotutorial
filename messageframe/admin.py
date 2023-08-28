from django.contrib import admin
from messageframe.models import Messagesframe
# Register your models here.
@admin.register(Messagesframe)
class UserAdmin(admin.ModelAdmin):
    list_display=['name','email','password']