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
        # font init
        self._fontNormal = None
        self._fontTitle = None
        
        # color init
        self.bgColor = "#282A36"
        self.fgColor = "#f8f8f2"
        self.highlightBg = "#6272a4"

        # entry init
        self.entryWidth = 640

    @property
    def fontNormal(self):
        if self._fontNormal is None:
            self._fontNormal = customtkinter.CTkFont(family="Arial", size=15)
        return self._fontNormal

    @property
    def fontTitle(self):
        if self._fontTitle is None:
            self._fontTitle = customtkinter.CTkFont(family="Arial", size=25, weight="bold")
        return self._fontTitle
    
    def _onResizeFont(self, width):
        actualSize = theme.fontNormal.cget("size")
        newSize = max(17, min(int(width / 50), 35))

        if abs(actualSize - newSize) < 5:
            return

        self.fontNormal.configure(size=newSize)
        self.fontTitle.configure(size=newSize + 10)

    def _onResizeEntry(self, width):
        self.entryWidth = max(200, width / 3)

    def onResize(self, width):
        self._onResizeFont(width)
        self._onResizeEntry(width)



    
theme = Theme()