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

def _updateEntrySize(widget):
    if isinstance(widget, customtkinter.CTkEntry):
        widget.configure(width=theme.entryWidth)

    for children in widget.winfo_children():
        _updateEntrySize(children)

def onResize(root):
    theme.onResize(root.winfo_width())

    for widget in root.winfo_children():
        _updateEntrySize(widget)