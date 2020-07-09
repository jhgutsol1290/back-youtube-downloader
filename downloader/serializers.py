from rest_framework import serializers
from .models import DownloadedVideos


class DownloadedVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadedVideos
        fields = "__all__"
