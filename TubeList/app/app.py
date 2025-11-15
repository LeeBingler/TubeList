"""
!/usr/bin/env python
-*- coding: utf-8 -*-

Code that manage all the tkinter window
"""
from app.utilsApp import chooseFile, handleDownload
from app.Theme import theme

import tkinter as tk
import customtkinter
from PIL import Image

def _initRoot():
    root = tk.Tk()
    root.title("TubeList")
    root.state("zoomed")
    root.geometry("1920x1080")
    root.minsize(480, 480)
    
    # Icon setting
    icon = tk.PhotoImage(file='./TubeList/images/icon.png') # load image from root of project
    root.iconphoto(True, icon)

    # Colors settings
    root.configure(background=theme.bgColor)
    root.option_add("*Background", theme.bgColor)
    root.option_add("*Foreground", theme.fgColor)
    root.option_add("*Highlightbackground", theme.highlightBg)
    return root

def _initTitle(root):
    title = customtkinter.CTkLabel(root, text="Welcome to TubeList")
    title.pack(anchor="center", pady=(50, 0))
    title.configure(font=theme.fontTitle)

    subtitle = customtkinter.CTkLabel(root, text="The best free and fast converter for Youtube video to MP3 format")
    subtitle.pack(anchor="center", pady=(10, 50))
    subtitle.configure(font=theme.fontSubtitle)
    return title

def _initURL(root):
    tk.Label(root, text="URL of the playlist / song:", font=theme.fontNormal).pack(anchor="center")
    entryUrl = customtkinter.CTkEntry(
        root,
        font=theme.fontNormal,
        width=theme.entryWidth + 400,
        placeholder_text="https://www.youtube.com/watch?v=<Your Video / Playlist>",
        placeholder_text_color=theme.placeholderColor
    )
    entryUrl.pack(pady=10, ipady=10, anchor="center")
    theme.registeredEntry["entryUrl"] = entryUrl

    return entryUrl

def _initPath(root):
    tk.Label(root, text="Where to download:", font=theme.fontNormal).pack(anchor="center", pady=(20, 0))
    fr1 = tk.Frame(root)
    fr1.pack(fill="y", anchor="center")
    entryPath = customtkinter.CTkEntry(
        fr1,
        font=theme.fontNormal,
        width=theme.entryWidth,
        placeholder_text="C:/Users/<Username>/Documents/",
        placeholder_text_color=theme.placeholderColor
    )
    entryPath.pack(padx=10, pady=10, ipady=10, side="left", anchor="center")
    theme.registeredEntry["entryPath"] = entryPath

    folderImage = customtkinter.CTkImage(
        light_image=Image.open('./TubeList/images/folder-icon-size_128.png'),
        dark_image=Image.open('./TubeList/images/folder-icon-size_128.png'),
        size=(32, 32)
    )

    buttonPath = customtkinter.CTkButton(
        fr1,
        text="Choose a folder",
        corner_radius=50,
        fg_color=theme.highlightBg,
        font=theme.fontNormal,
        image=folderImage,
        command=lambda: chooseFile(entryPath)
    )
    buttonPath.pack(side="left", anchor="center", ipady=10)

    return {"entry": entryPath, "button": buttonPath}

def _initDowload(root, url, entryPath):
    resultDownload = tk.StringVar(value="")
    downloadImage = customtkinter.CTkImage(
        light_image=Image.open('./TubeList/images/data-transfer-download-icon-size_64.png'),
        dark_image=Image.open('./TubeList/images/data-transfer-download-icon-size_64.png'),
        size=(32, 32)
    )

    btnDownload = customtkinter.CTkButton(
        root,
        text="Download",
        corner_radius=50,
        font=theme.fontNormal,
        fg_color=theme.btnDownloadFgColor,
        hover_color=theme.btnDownloadHoverColor,
        image=downloadImage,
        command=lambda: handleDownload(url=url.get(), path=entryPath.get(), resultDownload=resultDownload)
    )
    btnDownload.pack(anchor="center", pady=20, ipadx=15, ipady=15)

    return {"result": resultDownload, "button": btnDownload}

def app():
    root = _initRoot()

    title = _initTitle(root)
    entryUrl = _initURL(root)
    path = _initPath(root)
    download = _initDowload(root, entryUrl, path.get("entry"))

    logLabel = tk.Label(
        root,
        textvariable=download.get("result"),
        font=theme.fontNormal,
    )
    logLabel.pack(anchor="center", pady=30)

    tk.Label(root, text="Nothing will work unless you do.", font=theme.fontNormal).pack(anchor="center")
    tk.Label(root, text="- Maya Angelou", font=theme.fontNormal).pack(anchor="center")

    root.bind("<Configure>", lambda _: theme.onResize(root.winfo_width(), path.get("button").winfo_width()))
    root.mainloop()

    return 0