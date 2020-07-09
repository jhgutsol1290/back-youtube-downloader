from rest_framework.decorators import api_view
from rest_framework.response import Response

from application.controller import download_save_video, get_videos_list
from utils.responses import CustomResponse


@api_view(["GET", "POST"])
def download_list(request):
    if request.method == "GET":
        serializer = get_videos_list(request)
        return CustomResponse(
            message="Registros recuperados correctamente", data=serializer.data
        ).success()
    elif request.method == "POST":
        serializer = download_save_video(request)
        if serializer is None:
            return CustomResponse(message="Error al descargar el video").errors(
                status_code=500
            )
        return CustomResponse(
            message="Video descargado correctamente", data=serializer.data
        ).success(status_code=201)
