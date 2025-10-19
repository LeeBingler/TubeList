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

    return True

def downloadPlaylist(url: str, path: str):

    pl = Playlist(url)
    for video in pl.videos:
        print(video.title)
        _downloadAudio(video, path)
    return True

def downloadAny(url: str, path: str):
    try: 
        return downloadVideo(url, path)
    except RegexMatchError:
        try:
            return downloadPlaylist(url, path)
        except (RegexMatchError, KeyError):
            print("Url is not a valid youtube url")
        except Exception as e:
            print("downloadPlaylist: ", e)
    except Exception as e:
        print("downloadVideo: ", e)
    
    return False