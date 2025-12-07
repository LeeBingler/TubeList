"""
!/usr/bin/env python
-*- coding: utf-8 -*-

Code that manage all the tkinter window
"""
from app.utilsApp import chooseFile, notificationDownloadEnd
from app.Theme import theme
from app.Loadbars import LoadBars

import tkinter as tk
import customtkinter
from PIL import Image

from download import YouTubeDownloader
import threading

class TubeListApp:
    def __init__(self):
        self.root = self._initRoot()
        self.downloader = YouTubeDownloader("./", "mp3")

        # Widgets
        self.entryUrl = None
        self.entryPath = None
        self.buttonPath = None
        self.resultDownload = None
        self.loadBars = LoadBars(self.root)
        
        self.formats = ["mp3", "wav", "m4a", "flac", "aac", "opus"]
        self.formatVar = tk.StringVar(value="mp3")

        # UI build
        self._initTitle()
        self._initURL()
        self._initPath()
        self._initDownload()
        self.loadBars.init()
        self._initLog()
        self._initFooter()

        # Resize behavior
        self.root.bind("<Configure>", self._onResize)


    def _initRoot(self):
        root = tk.Tk()
        root.title("TubeList")
        root.state("zoomed")
        root.geometry("1920x1080")
        root.minsize(480, 480)

        # Icon
        icon = tk.PhotoImage(file='./TubeList/images/icon.png')
        root.iconphoto(True, icon)

        # Colors
        root.configure(background=theme.bgColor)
        root.option_add("*Background", theme.bgColor)
        root.option_add("*Foreground", theme.fgColor)
        root.option_add("*Highlightbackground", theme.highlightBg)

        return root


    def _initTitle(self):
        title = customtkinter.CTkLabel(self.root, text="Welcome to TubeList", font=theme.fontTitle)
        title.pack(anchor="center", pady=(50, 0))

        subtitle = customtkinter.CTkLabel(
            self.root,
            text="The best free and fast converter for Youtube playlist to MP3 format",
            font=theme.fontSubtitle
        )
        subtitle.pack(anchor="center", pady=(10, 50))


    def _initURL(self):
        tk.Label(self.root, text="URL of the playlist / song:", font=theme.fontNormal).pack(anchor="center")
        frame = tk.Frame(self.root)
        frame.pack(anchor="center")

        self.entryUrl = customtkinter.CTkEntry(
            frame,
            font=theme.fontNormal,
            width=theme.entryWidth + 400,
            placeholder_text="https://www.youtube.com/watch?v=<Your Playlist>",
            placeholder_text_color=theme.placeholderColor
        )
        self.entryUrl.pack(pady=10, ipady=10, anchor="center", side="left")
        theme.registeredEntry["entryUrl"] = self.entryUrl


        self.buttonFormat = customtkinter.CTkComboBox(
            master=frame,
            values=self.formats,
            variable=self.formatVar,
            font=theme.fontNormal,
            corner_radius=10,
            hover=True,
            button_hover_color=theme.highlightBg,
            dropdown_hover_color=theme.bgColor,
            fg_color=theme.highlightBg,
            dropdown_font=theme.fontNormal,
            state="readonly",
            height=70,
            width=170
        )
        self.buttonFormat.pack(side="right", pady=10, padx=10)

    def _initPath(self):
        tk.Label(self.root, text="Where to download:", font=theme.fontNormal).pack(anchor="center", pady=(20, 0))

        frame = tk.Frame(self.root)
        frame.pack(anchor="center", pady=10)

        self.entryPath = customtkinter.CTkEntry(
            frame,
            font=theme.fontNormal,
            width=theme.entryWidth,
            placeholder_text="C:/Users/<Username>/Documents/",
            placeholder_text_color=theme.placeholderColor
        )
        self.entryPath.pack(padx=10, ipady=10, side="left")
        theme.registeredEntry["entryPath"] = self.entryPath

        folderImg = customtkinter.CTkImage(
            light_image=Image.open('./TubeList/images/folder-icon-size_128.png'),
            dark_image=Image.open('./TubeList/images/folder-icon-size_128.png'),
            size=(32, 32)
        )

        self.buttonPath = customtkinter.CTkButton(
            frame,
            text="Choose a folder",
            font=theme.fontNormal,
            corner_radius=50,
            fg_color=theme.highlightBg,
            image=folderImg,
            command=lambda: chooseFile(self.entryPath)
        )
        self.buttonPath.pack(side="right", ipady=10)

    def _handleDownload(self):
        def run():
            self.loadBars.resetBars()

            self.downloader.path = self.entryPath.get()
            self.downloader.format = self.formatVar.get()
            self.downloader.set_progress_callbacks(self.loadBars.progressCallbackVideo, self.loadBars.progressCallbackPlaylist)

            resultDownload = self.downloader.download(self.entryUrl.get())

            if (resultDownload['ok']):
                self.resultDownload.set(f'"{resultDownload["title"]}" is downloaded')
            else:
                self.resultDownload.set(f'Error: {resultDownload["error"]}')
            notificationDownloadEnd(resultDownload)

        threading.Thread(target=run, daemon=True).start()

    def _initDownload(self):
        self.resultDownload = tk.StringVar(value="")

        downloadImg = customtkinter.CTkImage(
            light_image=Image.open('./TubeList/images/data-transfer-download-icon-size_64.png'),
            dark_image=Image.open('./TubeList/images/data-transfer-download-icon-size_64.png'),
            size=(32, 32)
        )

        button = customtkinter.CTkButton(
            self.root,
            text="Download",
            corner_radius=50,
            font=theme.fontNormal,
            fg_color=theme.btnDownloadFgColor,
            hover_color=theme.btnDownloadHoverColor,
            image=downloadImg,
            command=self._handleDownload
        )
        button.pack(anchor="center", pady=20, ipadx=15, ipady=15)


    def _initLog(self):
        tk.Label(self.root, textvariable=self.resultDownload, font=theme.fontNormal, wraplength=1500).pack(anchor="center", pady=30)


    def _initFooter(self):
        tk.Label(self.root, text="Nothing will work unless you do.", font=theme.fontNormal).pack(anchor="center")
        tk.Label(self.root, text="- Maya Angelou", font=theme.fontNormal).pack(anchor="center")


    def _onResize(self, event):
        theme.onResize(self.root.winfo_width(), self.buttonPath.winfo_width())


    def run(self):
        self.root.mainloop()
