from django.contrib import admin
from formapp.models import User
# Register your models here.
# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')