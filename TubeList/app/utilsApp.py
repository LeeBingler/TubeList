import customtkinter
import tkinter as tk
from plyer import notification

def chooseFile(entry):
    file = customtkinter.filedialog.askdirectory(title="Sélectionnez un dossier")

    if file:
        entry.delete(0, tk.END)
        entry.insert(0, file)

def notificationDownloadEnd(resultDownload):
    if (resultDownload['ok']):
        notification.notify(
            title = "TubeList",
            message = f"Your {resultDownload["type"]} is downloaded:\n{resultDownload["title"]}",
            ticker = "TubeList",
            app_icon = "./TubeList/images/icon.ico",
            timeout = 10,
            toast = False
        )
    else:
        notification.notify(
            title = "TubeList",
            message = "Error with the download",
            ticker = "TubeList",
            app_icon = "./TubeList/images/icon.ico",
            timeout = 10,
            toast = False
        )