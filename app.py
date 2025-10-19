"""
!/usr/bin/env python
-*- coding: utf-8 -*-

Code that manage all the tkinter window
"""
from download import downloadAny

import tkinter as tk
from tkinter import *
import customtkinter

def _chooseFile(entry):
    file = customtkinter.filedialog.askdirectory(title="Sélectionnez un dossier")

    if file:
        entry.delete(0, tk.END)
        entry.insert(0, file)

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

def _initTitle():
    title = tk.Label(text="MP3 YT playlist downloader")
    title.pack()

    title.config(font=("Arial", 25), pady=10)
    return title

def app():
    root = _initRoot()

    title = _initTitle()

    url = tk.StringVar()
    tk.Label(text="URL of the playlist / song").pack()
    entryUrl = customtkinter.CTkEntry(
        root,
        textvariable=url,
    )
    entryUrl.pack(pady=10)


    fr1 = tk.Frame(root)
    fr1.pack(fill="y", anchor="center")
    tk.Label(text="Where to download").pack()
    path = tk.StringVar()
    entryPath = customtkinter.CTkEntry(
        fr1,
        textvariable=path
    )
    entryPath.pack(pady=10, padx=10, side="left")

    buttonPath = customtkinter.CTkButton(
        fr1, 
        text="Choose a folder", 
        corner_radius=50,
        command=lambda: _chooseFile(entryPath)
    )
    buttonPath.pack(side="left") 


    btnDownload = customtkinter.CTkButton(
        root,
        text="Download",
        corner_radius=50,
        command=lambda: downloadAny(url=url.get(), path=path.get())
    )
    btnDownload.pack()

    # TODO: afficher la thumbnail de la video et le titre

    # TODO: afficher les logs d'erreur s'il y en a sans faire crash la fenetre

    # TODO: afficher progression du téléchargement

    tk.Label(root, text="Nothing will work unless you do.").pack()
    tk.Label(root, text="- Maya Angelou").pack()

    root.mainloop()