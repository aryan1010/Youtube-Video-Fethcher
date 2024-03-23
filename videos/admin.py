# myapp/admin.py
from django.contrib import admin
from .models import Video, APIKey

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'published_at')
    list_filter = ('published_at',)
    search_fields = ('title', 'description')
    ordering = ('-published_at',)

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'is_active')