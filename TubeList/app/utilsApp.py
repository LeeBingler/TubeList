import customtkinter
import tkinter as tk
from plyer import notification

def chooseFile(entry):
    file = customtkinter.filedialog.askdirectory(title="Sélectionnez un dossier")

    if file:
        entry.delete(0, tk.END)
        entry.insert(0, file)

def notificationDownloadEnd(resultDownload):
    title = "TubeList"
    icon = "./TubeList/images/icon.ico"

    if resultDownload["ok"]:
        msg = f"Your {resultDownload['type']} is downloaded:\n{resultDownload['title']}"
    else:
        msg = "Error with the download"

    notification.notify(
        title=title,
        message=msg,
        ticker=title,
        app_icon=icon,
        timeout=10,
        toast=False
    )