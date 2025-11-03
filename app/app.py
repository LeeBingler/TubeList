"""
!/usr/bin/env python
-*- coding: utf-8 -*-

Code that manage all the tkinter window
"""
from app.utilsApp import chooseFile, handleDownload, onResize
from app.Theme import theme

import tkinter as tk
import customtkinter

def _initRoot():
    root = tk.Tk()
    root.title("MP3 playlist downloader")
    root.state("zoomed")
    root.geometry("1920x1080")

    # Colors settings
    root.configure(background=theme.bgColor)
    root.option_add("*Background", theme.bgColor)
    root.option_add("*Foreground", theme.fgColor)
    root.option_add("*Highlightbackground", theme.highlightBg)
    return root

def _initTitle(root):
    title = customtkinter.CTkLabel(root, text="MP3 YT playlist downloader")
    title.pack()

    title.configure(pady=10)
    return title

def _initURL(root):
    url = tk.StringVar()
    tk.Label(text="URL of the playlist / song", font=theme.fontNormal).pack()
    entryUrl = customtkinter.CTkEntry(
        root,
        textvariable=url,
        font=theme.fontNormal,
        width=theme.entryWidth
    )
    entryUrl.pack(pady=10)

    return [url, entryUrl]

def app():
    root = _initRoot()

    title = _initTitle(root)
    title.configure(font=theme.fontTitle)

    url = _initURL(root)

    tk.Label(text="Where to download", font=theme.fontNormal).pack()
    fr1 = tk.Frame(root)
    fr1.pack(fill="y", anchor="center")
    path = tk.StringVar()
    entryPath = customtkinter.CTkEntry(
        fr1,
        textvariable=path,
        font=theme.fontNormal,
        width=theme.entryWidth
    )
    entryPath.pack(pady=10, padx=10, side="left")

    buttonPath = customtkinter.CTkButton(
        fr1,
        text="Choose a folder",
        corner_radius=50,
        fg_color="#6272a4",
        font=theme.fontNormal,
        command=lambda: chooseFile(entryPath)
    )
    buttonPath.pack(side="left")

    resultDownload = tk.StringVar(value="")
    logLabel = tk.Label(
        root,
        textvariable=resultDownload,
        font=theme.fontNormal,
    )
    btnDownload = customtkinter.CTkButton(
        root,
        text="Download",
        corner_radius=50,
        fg_color="#6272a4",
        font=theme.fontNormal,
        command=lambda: handleDownload(url=url[0].get(), path=path.get(), resultDownload=resultDownload)
    )
    btnDownload.pack()
    logLabel.pack()

    tk.Label(root, text="Nothing will work unless you do.", font=theme.fontNormal).pack()
    tk.Label(root, text="- Maya Angelou", font=theme.fontNormal).pack()


    root.bind("<Configure>", lambda _: onResize(root))
    root.mainloop()

    return 0