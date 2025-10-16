#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Code to download audio

from pytubefix.cli import on_progress # type: ignore
from pytubefix import Playlist, YouTube # type: ignore


def downloadVideo(url: str, path: str):
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    ys = yt.streams.get_audio_only()
    ys.download(output_path=path)

def downloadPlaylist(url: str, path: str):
    pl = Playlist(url)
    for video in pl.videos:
        print(video.title)
        ys = video.streams.get_audio_only()
        ys.download(output_path=path)
