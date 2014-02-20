__author__ = 'Andres Moreno'
import wx
import splash


modules = {u'financial_parser': [0, '', u'financial_parser.py'],
           u'mainWindow': [1, 'Cascabel - Sistema de auditoria', u'mainWindow'],
           u'project_handle': [0, '', u'../project_handle.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = splash.MySplashScreen()
        self.main.Show()
        self.SetTopWindow(self.main)
        return True


def main():
    application = BoaApp(0)
    application.MainLoop()


if __name__ == "__main__":
    main()
