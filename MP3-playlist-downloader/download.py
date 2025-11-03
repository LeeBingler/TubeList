#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Code to download audio

from pytubefix.cli import on_progress
from pytubefix import Playlist, YouTube
from pytubefix.exceptions import RegexMatchError

def _downloadAudio(obj, path: str):
    stream = obj.streams.get_audio_only()
    stream.download(output_path=path)

def downloadVideo(url: str, path: str):
    yt = YouTube(url, on_progress_callback=on_progress)

    print(yt.title)
    _downloadAudio(yt, path)

    return yt.title

def downloadPlaylist(url: str, path: str):
    pl = Playlist(url)
    listTitle = []

    for video in pl.videos:
        print(video.title)
        _downloadAudio(video, path)
        listTitle.append(video.title)

    return listTitle

def downloadAny(url: str, path: str):
    title = ""
    try: 
        title = downloadVideo(url, path)
        return f"Downloaded : {title}"
    except RegexMatchError:
        try:
            title = downloadPlaylist(url, path)
            return f"Downloaded : {title} "
        except (RegexMatchError, KeyError) as e:
            return f"404: Url is not a valid youtube url {e}"
        except Exception as e:
            print("downloadPlaylist: ", e)
            return e
    except Exception as e:
        print("downloadVideo: ", e)
        return e

    return False