#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Code to download audio

from pytubefix import Playlist, YouTube
from pytubefix.exceptions import RegexMatchError, BotDetection
import os
import subprocess


def _downloadAudio(obj, path: str, format: str):
    stream = obj.streams.get_audio_only()
    downloaded = stream.download(output_path=path)

    if (format == "m4a"): return downloaded

    base, ext = os.path.splitext(downloaded)
    output_file = f"{base}.{format}"
    print(output_file)

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

def _on_progress(stream, chunk: bytes, bytes_remaining: int, progressCallbackVideo):
    filesize = stream.filesize
    bytes_received = filesize - bytes_remaining
    percent = bytes_received / filesize

    if progressCallbackVideo:
        progressCallbackVideo(percent=percent)

def _downloadVideo(url: str, path: str, progressCallbackVideo, format):
    yt = YouTube(
        url, 
        'WEB', 
        on_progress_callback = lambda stream, chunk, bytes_remaining: _on_progress(stream, chunk, bytes_remaining, progressCallbackVideo)
    )

    print(yt.title)
    _downloadAudio(yt, path, format)

    return yt.title

def _downloadPlaylist(url: str, path: str, progressCallbackVideo ,progressCallbackPlaylist, format):
    pl = Playlist(url)
    total = len(pl.videos)

    for index, video in enumerate(pl.videos):
        if progressCallbackPlaylist:
            progressCallbackPlaylist(index, total)

        _downloadVideo(video.watch_url, path, progressCallbackVideo, format)

    if progressCallbackPlaylist:
        progressCallbackPlaylist(total, total)

    print(pl.title)
    return pl.title

def _checkPath(path: str):
    if path == "":
        path = "./"
        return False

    if os.path.isdir(path):
        return False
    
    return True

def downloadAny(url: str, path: str, progressCallbackVideo: function, progressCallbackPlaylist: function, format: str):
    if url == None or path == None or progressCallbackVideo == None or progressCallbackPlaylist == None:
        print(f"Missing argument {url}, {path}, {progressCallbackVideo}, {progressCallbackPlaylist}")
        return f"Missing argument {url}, {path}, {progressCallbackVideo}, {progressCallbackPlaylist}"

    path = path.strip()
    url = url.strip()
    title = ""
    typeDownload = ""

    if _checkPath(path):
        return "Path is not valid"

    try: 
        title = _downloadVideo(url, path, progressCallbackVideo, format)
        typeDownload = "video"
        return {"title" : title, "type" : typeDownload}
    except RegexMatchError:
        try:
            title = _downloadPlaylist(url, path, progressCallbackVideo, progressCallbackPlaylist, format)
            typeDownload = "playlist"
            return {"title" : title, "type" : typeDownload, "ok" : True}
        except (RegexMatchError, KeyError) as e:
            return {"error": f"404: Url is not a valid youtube url\n\n{e}", "ok" : False}
        except BotDetection as e:
            return {"error": f"403: This request was detected as a bot (too much request).\nYou should use another wifi to download\n\n{e}", "ok" : False}
        except Exception as e:
            print("downloadPlaylist: ", e)
            return {"error": e, "ok": False}
    except BotDetection as e:
        return {"error": f"403: This request was detected as a bot (too much request).\nYou should use another wifi to download\n\n{e}", "ok" : False}
    except Exception as e:
        print("Error downloadVideo: ", e)
        return {"error": e, "ok": False}