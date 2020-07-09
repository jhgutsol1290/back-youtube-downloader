from django.db import models

# Create your models here.
class DownloadedVideos(models.Model):
    author = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=255, blank=False, default="")
    link = models.CharField(max_length=100, blank=False)
    created = models.DateField(auto_now_add=True, null=True, blank=True)
