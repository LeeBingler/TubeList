"""
!/usr/bin/env python
-*- coding: utf-8 -*-

Code that manage all the tkinter window
"""
from download import downloadPlaylist


import tkinter as tk
from tkinter import *
import customtkinter

def chooseFile(entry):
    file = customtkinter.filedialog.askdirectory(title="Sélectionnez un dossier")

    if file:
        entry.delete(0, tk.END)
        entry.insert(0, file)

def app():
    root = tk.Tk()
    root.title("MP3 playlist downloader")
    root.state("zoomed")

    url = tk.StringVar()
    tk.Label(text="URL of the playlist / song").pack()
    entryUrl = customtkinter.CTkEntry(
        root,
        textvariable=url,
    )
    entryUrl.pack(pady=10)


    tk.Label(text="Where to download").pack()
    path = tk.StringVar()
    entryPath = customtkinter.CTkEntry(
        root,
        textvariable=path
    )
    entryPath.pack(pady=10)

    buttonPath = customtkinter.CTkButton(
        root, 
        text="Choisir un dossier", 
        corner_radius=50,
        command=lambda: chooseFile(entryPath)
    )
    buttonPath.pack() 


    btnDownload = customtkinter.CTkButton(
        root,
        text="Download",
        corner_radius=50,
        command=lambda: downloadPlaylist(url=url.get(), path=path.get())
    )
    btnDownload.pack()

    # TODO: afficher les logs d'erreur s'il y en a sans faire crash la fenetre

    tk.Label(root, text="Nothing will work unless you do.").pack()
    tk.Label(root, text="- Maya Angelou").pack()

    root.mainloop()