from django.contrib import admin
from .models import ScreenControl

@admin.register(ScreenControl)
class ScreenControlAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'is_active', 'updated_at')
    list_filter = ('is_active', 'updated_at')
    search_fields = ('title', 'city')
