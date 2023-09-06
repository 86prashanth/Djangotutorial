from django.contrib import admin
from .models import Page,Like,Post,Song
# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['page_name','page_cat','page_publish_date']
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=['like']
    
@admin.register(Post)
class LikeAdmin(admin.ModelAdmin):
    list_display=['post_title','post_cat','post_publish_date']
    
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=['song_name','song_duration','written_by']