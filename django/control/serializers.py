from rest_framework import serializers
from .models import ScreenControl

class ScreenControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenControl
        fields = ['id', 'title', 'city', 'temperature', 'weather', 'news', 'is_active', 'updated_at']
