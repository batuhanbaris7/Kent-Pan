from django.db import models

class ScreenControl(models.Model):
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    temperature = models.CharField(max_length=10, blank=True, null=True)
    weather = models.CharField(max_length=100, blank=True, null=True)
    news = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
