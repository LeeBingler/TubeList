"""
!/usr/bin/env python
-*- coding: utf-8 -*-

Loadbar
"""
import tkinter as tk
import customtkinter

from app.Theme import theme

class LoadBar:
    def __init__(self, parent, label_text="Progress", width=800, color=None):
        self.parent = parent
        self.width = width
        self.color = color or theme.btnDownloadFgColor
        self.label_text = label_text

        self.frame = tk.Frame(self.parent, width=theme.loadbarWidth)
        self.frame.pack(anchor="center", pady=10)

        # ProgressBar
        self.bar = customtkinter.CTkProgressBar(self.frame, width=self.width, progress_color=self.color)
        self.bar.pack(pady=10, side="right", fill="x")
        self.bar.set(0)

        # Label
        self.var = tk.StringVar(value=f"{self.label_text}: 0%")
        self.label = customtkinter.CTkLabel(self.frame, textvariable=self.var, font=theme.fontNormal)
        self.label.pack(side="left", ipadx=15)

    def reset(self):
        self.bar.set(0)
        self.var.set(f"{self.label_text}: 0%")

    def set(self, percent: float):
        percent = max(0, min(percent, 1))
        self.bar.set(percent)
        self.var.set(f"{self.label_text}: {int(percent * 100)}%")

class LoadBars:
    def __init__(self, parent):
        self.parent = parent

        self.video = None
        self.playlsit = None

    def progressCallbackVideo(self, percent):
        self.video.set(percent)

    def progressCallbackPlaylist(self, index, total):
        percent = index / total
        self.playlist.set(percent)

    def resetBars(self):
        self.video.reset()
        self.playlist.reset()

    def init(self):
        self.video = LoadBar(self.parent, "Video")
        self.playlist = LoadBar(self.parent, "Playlist")

        theme.loadbar = self.video.bar
        theme.loadbarPlaylist = self.playlist.bar