#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Code to download audio

from pytubefix import Playlist, YouTube
from pytubefix.exceptions import RegexMatchError, BotDetection
import os
import subprocess

class YouTubeDownloader:
    def __init__(self, path: str, format: str = "m4a"):
        self.path = path.strip() if path else "./"
        self.format = format
        self.progressCallbackVideo = None
        self.progressCallbackPlaylist = None

    def set_progress_callbacks(self, video_callback=None, playlist_callback=None):
        self.progressCallbackVideo = video_callback
        self.progressCallbackPlaylist = playlist_callback

    def _check_path(self):
        if not self.path:
            self.path = "./"
            return False
        if os.path.isdir(self.path):
            return False
        return True

    def _download_audio(self, yt_obj):
        stream = yt_obj.streams.get_audio_only()
        downloaded = stream.download(output_path=self.path)

        if self.format == "m4a":
            return downloaded

        base, ext = os.path.splitext(downloaded)
        output_file = f"{base}.{self.format}"
        print(f"Converting to {output_file}...")

        subprocess.run([
            "ffmpeg", "-y",
            "-i", downloaded,
            output_file
        ])

        try:
            os.remove(downloaded)
        except:
            pass

        return output_file

    def _on_progress(self, stream, chunk: bytes, bytes_remaining: int):
        filesize = stream.filesize
        bytes_received = filesize - bytes_remaining
        percent = bytes_received / filesize

        if self.progressCallbackVideo:
            self.progressCallbackVideo(percent=percent)

    def _download_video(self, url: str):
        yt = YouTube(
            url, 
            'WEB',
            on_progress_callback=lambda s, c, b: self._on_progress(s, c, b)
        )

        print(f"Downloading video: {yt.title}")
        self._download_audio(yt)
        return yt.title

    def _download_playlist(self, url: str):
        pl = Playlist(url)
        total = len(pl.videos)

        for index, video in enumerate(pl.videos):
            if self.progressCallbackPlaylist:
                self.progressCallbackPlaylist(index, total)

            self._download_video(video.watch_url)

        if self.progressCallbackPlaylist:
            self.progressCallbackPlaylist(total, total)

        print(f"Downloaded playlist: {pl.title}")
        return pl.title

    def download(self, url: str):
        if not url or self._check_path():
            return {"error": "Invalid path or URL", "ok": False}

        url = url.strip()
        try:
            title = self._download_video(url)
            return {"title": title, "type": "video", "ok": True}
        except RegexMatchError:
            try:
                title = self._download_playlist(url)
                return {"title": title, "type": "playlist", "ok": True}
            except (RegexMatchError, KeyError) as e:
                return {"error": f"404: URL is not valid\n\n{e}", "ok": False}
            except BotDetection as e:
                return {"error": f"403: Bot detection triggered\n{e}", "ok": False}
            except Exception as e:
                return {"error": str(e), "ok": False}
        except BotDetection as e:
            return {"error": f"403: Bot detection triggered\n{e}", "ok": False}
        except Exception as e:
            return {"error": str(e), "ok": False}
