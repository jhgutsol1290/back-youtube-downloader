from typing import Dict

from rest_framework.response import Response

from downloader.models import DownloadedVideos
from downloader.serializers import DownloadedVideosSerializer
from utils.responses import CustomResponse
from utils.youtube_downloader import Downloader
from utils.paginator import StandardResultsSetPagination


def get_videos_list(request: Dict) -> list:
    downloaded_videos = videos_queryset(request=request)
    paginator = StandardResultsSetPagination()
    result_page = paginator.paginate_queryset(downloaded_videos, request)
    serializer = DownloadedVideosSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


def download_save_video(request: Dict) -> Dict:
    link = request.data.get("link", None)
    video_name = request.data.get("video_name", None)
    downloader = Downloader(link=link, video_name=video_name)
    if not downloader.perform_download():
        return None
    data = downloader.get_video_data()
    serializer = DownloadedVideosSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return serializer


def videos_queryset(request: Dict) -> list:
    filter_date = request.query_params.get("filter_date", None)
    title = request.query_params.get("title", None)
    if filter_date and title is None:
        downloaded_videos = DownloadedVideos.objects.filter(
            created=filter_date
        )
    elif title and filter_date is None:
        downloaded_videos = DownloadedVideos.objects.filter(
            title__icontains=title
        )
    elif filter_date and title:
        downloaded_videos = DownloadedVideos.objects.filter(
            created=filter_date, title__icontains=title
        )
    else:
        downloaded_videos = DownloadedVideos.objects.all()
    return downloaded_videos.order_by("-id")
