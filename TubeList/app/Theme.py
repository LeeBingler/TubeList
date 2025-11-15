"""
!/usr/bin/env python
-*- coding: utf-8 -*-

Code that manage theme of tkinter window
"""
import customtkinter

class Theme():
    """Global theme for Singleton"""
    _instance = None  # singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_theme()
        return cls._instance

    def _init_theme(self):
        self._lastWidthWindow = -1000

        # font init
        self._fontNormal = None
        self._fontTitle = None
        self._fontSubtitle = None
        self.fontNormalSize = 15
        self.fontFamily = "Poplar Std"
        
        # color init
        self.bgColor = "#282A36"
        self.fgColor = "#f8f8f2"
        self.highlightBg = "#6272a4"
        self.btnDownloadFgColor = "#b2071d"
        self.btnDownloadHoverColor = "#640512"
        self.placeholderColor = "#919191"

        # entry init
        self.registeredEntry = {}
        self.entryWidth = 640
        self.ipadyEntry = 10

    @property
    def fontNormal(self):
        if self._fontNormal is None:
            self._fontNormal = customtkinter.CTkFont(family=self.fontFamily, size=15)
        return self._fontNormal

    @property
    def fontTitle(self):
        if self._fontTitle is None:
            self._fontTitle = customtkinter.CTkFont(family=self.fontFamily, size=25, weight="bold")
        return self._fontTitle
    
    @property
    def fontSubtitle(self):
        if self._fontSubtitle is None:
            self._fontSubtitle = customtkinter.CTkFont(family=self.fontFamily, size=7)
        return self._fontSubtitle
    
    def _onResizeFont(self, width):
        actualSize = self.fontNormalSize
        newSize = max(20, min(int(width / 50), 40))

        if abs(actualSize - newSize) < 5:
            return

        self.fontNormalSize = newSize
        self.fontNormal.configure(size=newSize)
        self.fontTitle.configure(size=newSize + 15)
        self.fontSubtitle.configure(size=newSize - 7)

    def _onResizeEntry(self, width, buttonPathWidth):
        self.entryWidth = max(200, width / 3)
        self.ipadyEntry = max(9, int(self.fontNormalSize / 2))

        urlEntry = self.registeredEntry.get("entryUrl")
        urlEntry.configure(width=self.entryWidth + buttonPathWidth)

        pathEntry = self.registeredEntry.get("entryPath")
        pathEntry.configure(width=self.entryWidth)


    def onResize(self, width, buttonPathWidth):
        if abs(width - self._lastWidthWindow) < 5:
            return
        
        if buttonPathWidth == 1:
            buttonPathWidth = 339

        self._lastWidthWindow = width
        self._onResizeFont(width)
        self._onResizeEntry(width, buttonPathWidth)


theme = Theme()