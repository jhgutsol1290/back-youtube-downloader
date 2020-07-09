import time
from typing import Dict

from pytube import YouTube
from pytube.cli import on_progress


class Downloader:
    def __init__(
        self,
        save_path: str = "/home/jgutierrez/Desktop/youtube_downloader/downloads_test",
        link: str = None,
        video_name: str = None,
    ) -> None:
        self.save_path = save_path
        self.link = link
        self.video_name = video_name

    def perform_download(self) -> bool:
        try:
            if self.link is None or self.video_name is None:
                raise Exception
            yt = YouTube(self.link)
            self.author = yt.author
            self.title = self.video_name
            title_to_save = f"{self.video_name}_{time.time()}"
            yt.streams.filter(progressive=True, file_extension="mp4").order_by(
                "resolution"
            ).desc().first().download(
                output_path=self.save_path, filename=title_to_save
            )
            return True
        except Exception as e:
            return False

    def get_video_data(self) -> Dict:
        return {"title": self.title, "link": self.link, "author": self.author}
