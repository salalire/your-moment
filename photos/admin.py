from django.contrib import admin
from .models import Photo
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image', 'created_at', 'updated_at', 'album')    

# Register your models here.
