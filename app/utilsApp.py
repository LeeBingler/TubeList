from download import downloadAny
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

def onResize(root, fonts):
    actualSize = fonts["fontNormal"].cget("size")
    newSize = max(17, min(int(root.winfo_width() / 50), 35))

    print(actualSize, newSize)

    if abs(actualSize - newSize) < 5:
        return

    fonts["fontNormal"].configure(size=newSize)
    fonts["fontTitle"].configure(size=newSize + 10)