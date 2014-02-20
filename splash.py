import wx
import mainWindow


class MySplashScreen(wx.SplashScreen):
    """
Create a splash screen widget.
    """
    def __init__(self, parent=None):
        aBitmap = wx.Image(name = "resources/images/splash.png").ConvertToBitmap()
        splashStyle = wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT
        splashDuration = 3000 # milliseconds
        wx.SplashScreen.__init__(self, aBitmap, splashStyle,
                                 splashDuration, parent)
        self.Bind(wx.EVT_CLOSE, self.OnExit)

        wx.Yield()
#----------------------------------------------------------------------#

    def OnExit(self, evt):
        self.Hide()
        self.main = mainWindow.create(None)
        self.main.Show(True)
        evt.Skip()  