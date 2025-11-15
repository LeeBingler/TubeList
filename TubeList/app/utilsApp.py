from download import downloadAny
from app.Theme import theme
import customtkinter
import tkinter as tk

def chooseFile(entry):
    file = customtkinter.filedialog.askdirectory(title="Sélectionnez un dossier")

    if file:
        entry.delete(0, tk.END)
        entry.insert(0, file)

def handleDownload(url, path, resultDownload):
    result = downloadAny(url, path)
    resultDownload.set(result)