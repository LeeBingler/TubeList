"""
!/usr/bin/env python
-*- coding: utf-8 -*-

Code that manage all the tkinter window
"""
from app.utilsApp import chooseFile, handleDownload, onResize

import tkinter as tk
from tkinter import font
import customtkinter

def _initRoot():
    root = tk.Tk()
    root.title("MP3 playlist downloader")
    root.state("zoomed")
    root.geometry("1920x1080")

    # Colors settings
    root.configure(background="#282A36")
    root.option_add("*Background", "#282A36")
    root.option_add("*Foreground", "#f8f8f2")
    root.option_add("*Highlightbackground", "	#6272a4")
    return root

def _initTitle(root):
    title = customtkinter.CTkLabel(root, text="MP3 YT playlist downloader")
    title.pack()

    title.configure(pady=10)
    return title

def app():
    root = _initRoot()
    fontSizes = {"fontNormal": customtkinter.CTkFont(family="Arial", size=15),
                  "fontTitle": customtkinter.CTkFont(family="Arial", size=25, weight="bold")
    }

    title = _initTitle(root)
    title.configure(font=fontSizes["fontTitle"])

    url = tk.StringVar()
    tk.Label(text="URL of the playlist / song", font=fontSizes["fontNormal"]).pack()
    entryUrl = customtkinter.CTkEntry(
        root,
        textvariable=url,
        font=fontSizes["fontNormal"]
    )
    entryUrl.pack(pady=10)


    tk.Label(text="Where to download", font=fontSizes["fontNormal"]).pack()
    fr1 = tk.Frame(root)
    fr1.pack(fill="y", anchor="center")
    path = tk.StringVar()
    entryPath = customtkinter.CTkEntry(
        fr1,
        textvariable=path,
        font=fontSizes["fontNormal"]
    )
    entryPath.pack(pady=10, padx=10, side="left")

    buttonPath = customtkinter.CTkButton(
        fr1, 
        text="Choose a folder", 
        corner_radius=50,
        fg_color="#6272a4",
        font=fontSizes["fontNormal"],
        command=lambda: chooseFile(entryPath)
    )
    buttonPath.pack(side="left") 

    resultDownload = tk.StringVar(value="")
    logLabel = tk.Label(
        root,
        textvariable=resultDownload,
        font=fontSizes["fontNormal"],
    )
    btnDownload = customtkinter.CTkButton(
        root,
        text="Download",
        corner_radius=50,
        fg_color="#6272a4",
        font=fontSizes["fontNormal"],
        command=lambda: handleDownload(url=url.get(), path=path.get(), resultDownload=resultDownload)
    )
    btnDownload.pack()
    logLabel.pack()

    tk.Label(root, text="Nothing will work unless you do.", font=fontSizes["fontNormal"]).pack()
    tk.Label(root, text="- Maya Angelou", font=fontSizes["fontNormal"]).pack()


    root.bind("<Configure>", lambda e: onResize(root, fonts=fontSizes))
    root.mainloop()

    return 0