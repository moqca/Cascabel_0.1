#Boa:Dialog:genDocType

import wx

def create(parent):
    return genDocType(parent)

[wxID_GENDOCTYPE, wxID_GENDOCTYPEBTMAKE, wxID_GENDOCTYPEBUTTON1, 
 wxID_GENDOCTYPEDATEPICKERCTRL1, wxID_GENDOCTYPEDOCNAME, 
 wxID_GENDOCTYPEDOCPANEL, wxID_GENDOCTYPEDOCTITLE, wxID_GENDOCTYPEFROMACT, 
 wxID_GENDOCTYPEINDSELECT, wxID_GENDOCTYPEPROPANEL, 
 wxID_GENDOCTYPESELAUXILIAR, wxID_GENDOCTYPESELSUMARIA, 
 wxID_GENDOCTYPESTATICTEXT1, wxID_GENDOCTYPESTATICTEXT2, 
 wxID_GENDOCTYPESTATICTEXT3, wxID_GENDOCTYPESTATICTEXT4, 
 wxID_GENDOCTYPESTATICTEXT5, wxID_GENDOCTYPESTTEXT, wxID_GENDOCTYPETOACT, 
] = [wx.NewId() for _init_ctrls in range(19)]

class genDocType(wx.Dialog):
    def _init_coll_gridSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.selAuxiliar, 0, border=0, flag=0)
        parent.AddWindow(self.selSumaria, 0, border=0, flag=0)

    def _init_sizers(self):
        # generated method, don't edit
        self.gridSizer1 = wx.GridSizer(cols=0, hgap=0, rows=1, vgap=0)

        self._init_coll_gridSizer1_Items(self.gridSizer1)

        self.docPanel.SetSizer(self.gridSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_GENDOCTYPE, name=u'genDocType',
              parent=prnt, pos=wx.Point(291, 192), size=wx.Size(401, 488),
              style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Selecciona Tipo de Documento')
        self.SetClientSize(wx.Size(393, 461))

        self.docTitle = wx.StaticText(id=wxID_GENDOCTYPEDOCTITLE,
              label=u'Tipo de Documento', name=u'docTitle', parent=self,
              pos=wx.Point(16, 8), size=wx.Size(155, 24), style=0)
        self.docTitle.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Franklin Gothic Book'))

        self.docPanel = wx.Panel(id=wxID_GENDOCTYPEDOCPANEL, name=u'docPanel',
              parent=self, pos=wx.Point(24, 40), size=wx.Size(344, 128),
              style=wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.docPanel.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.docPanel.SetLabel(u'Document Types')
        self.docPanel.SetHelpText(u'')
        self.docPanel.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)

        self.staticText1 = wx.StaticText(id=wxID_GENDOCTYPESTATICTEXT1,
              label=u'Propiedades', name='staticText1', parent=self,
              pos=wx.Point(24, 184), size=wx.Size(79, 20), style=0)
        self.staticText1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Franklin Gothic Book'))

        self.proPanel = wx.Panel(id=wxID_GENDOCTYPEPROPANEL, name=u'proPanel',
              parent=self, pos=wx.Point(32, 216), size=wx.Size(336, 184),
              style=wx.TAB_TRAVERSAL)

        self.staticText2 = wx.StaticText(id=wxID_GENDOCTYPESTATICTEXT2,
              label=u'Desde Cuenta', name='staticText2', parent=self.proPanel,
              pos=wx.Point(8, 8), size=wx.Size(68, 13), style=0)

        self.fromAct = wx.ComboBox(choices=[], id=wxID_GENDOCTYPEFROMACT,
              name=u'fromCta', parent=self.proPanel, pos=wx.Point(8, 24),
              size=wx.Size(130, 21), style=0, value=u'')
        self.fromAct.SetLabel(u'')
        self.fromAct.Bind(wx.EVT_TEXT, self.OnFromActText,
              id=wxID_GENDOCTYPEFROMACT)
        self.fromAct.Bind(wx.EVT_COMBOBOX, self.OnFromActCombobox,
              id=wxID_GENDOCTYPEFROMACT)
        self.fromAct.Bind(wx.EVT_CHAR, self.OnFromActCombobox,
              id=wxID_GENDOCTYPEFROMACT)

        self.staticText3 = wx.StaticText(id=wxID_GENDOCTYPESTATICTEXT3,
              label=u'Hasta Cuenta', name='staticText3', parent=self.proPanel,
              pos=wx.Point(176, 8), size=wx.Size(66, 13), style=0)

        self.toAct = wx.ComboBox(choices=[], id=wxID_GENDOCTYPETOACT,
              name=u'toAct', parent=self.proPanel, pos=wx.Point(176, 24),
              size=wx.Size(130, 21), style=0, value=u'')
        self.toAct.SetLabel(u'')
        self.toAct.Bind(wx.EVT_TEXT, self.OnToActText,
              id=wxID_GENDOCTYPEFROMACT)
        self.toAct.Bind(wx.EVT_COMBOBOX, self.OnToActCombobox,
              id=wxID_GENDOCTYPEFROMACT)
        self.toAct.Bind(wx.EVT_CHAR, self.OnToActCombobox,
              id=wxID_GENDOCTYPEFROMACT)

        self.staticText4 = wx.StaticText(id=wxID_GENDOCTYPESTATICTEXT4,
              label=u'Nombre del Archivo', name='staticText4',
              parent=self.proPanel, pos=wx.Point(16, 144), size=wx.Size(93, 13),
              style=0)

        self.docName = wx.TextCtrl(id=wxID_GENDOCTYPEDOCNAME, name=u'docName',
              parent=self.proPanel, pos=wx.Point(8, 160), size=wx.Size(290, 21),
              style=0, value=u'')

        self.staticText5 = wx.StaticText(id=wxID_GENDOCTYPESTATICTEXT5,
              label=u'Desde', name='staticText5', parent=self.proPanel,
              pos=wx.Point(8, 64), size=wx.Size(30, 13), style=0)

        self.datePickerCtrl1 = wx.DatePickerCtrl(id=wxID_GENDOCTYPEDATEPICKERCTRL1,
              name='datePickerCtrl1', parent=self.proPanel, pos=wx.Point(8, 80),
              size=wx.Size(96, 21), style=wx.DP_SHOWCENTURY)

        self.btMake = wx.Button(id=wx.ID_OK, label=u'Generar', name=u'btMake',
              parent=self, pos=wx.Point(200, 432), size=wx.Size(75, 23),
              style=0)
        self.btMake.Bind(wx.EVT_BUTTON, self.OnBtMakeButton, id=wx.ID_OK)

        self.button1 = wx.Button(id=wx.ID_CANCEL, label=u'Cancel',
              name='button1', parent=self, pos=wx.Point(296, 432),
              size=wx.Size(75, 23), style=0)

        self.selAuxiliar = wx.RadioButton(id=wxID_GENDOCTYPESELAUXILIAR,
              label=u'Auxiliar', name=u'selAuxiliar', parent=self.docPanel,
              pos=wx.Point(0, 0), size=wx.Size(81, 13), style=0)
        self.selAuxiliar.SetValue(True)
        self.selAuxiliar.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Franklin Gothic Book'))

        self.selSumaria = wx.RadioButton(id=wxID_GENDOCTYPESELSUMARIA,
              label=u'Sumaria', name=u'selSumaria', parent=self.docPanel,
              pos=wx.Point(171, 0), size=wx.Size(69, 13), style=0)
        self.selSumaria.SetValue(False)
        self.selSumaria.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Franklin Gothic Book'))

        self.stText = wx.StaticText(id=wxID_GENDOCTYPESTTEXT, label=u'Indice',
              name=u'stText', parent=self.proPanel, pos=wx.Point(16, 104),
              size=wx.Size(29, 13), style=0)

        self.indSelect = wx.ComboBox(choices=[], id=wxID_GENDOCTYPEINDSELECT,
              name=u'indSelect', parent=self.proPanel, pos=wx.Point(8, 120),
              size=wx.Size(288, 21), style=0, value=u'')
        self.indSelect.SetLabel(u'')

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.btMake.SetDefault()

    def OnBtMakeButton(self, event):
        self.to_act =  self.toAct.GetValue()
        self.from_act = self.fromAct.GetValue()
        self.start_date = self.datePickerCtrl1.GetValue()
        self.doc_name = self.docName.GetValue()
        self.choice = self.selAuxiliar.GetValue()

        if self.fromAct.GetValue() > self.toAct.GetValue():
            dlg = wx.MessageDialog(self,
                "La cuenta inicial no puede ser mayor a la final",
                "Confirmar", wx.OK)
            result = dlg.ShowModal()
            dlg.Destroy()
            if result != wx.ID_OK:
                self.Destroy()
        self.Destroy()

    def SetAccounts(self, accounts):
        self.acts = list(set(accounts))
        self.acts.sort()
        self.fromAct.SetItems(self.acts)
        self.toAct.SetItems(self.acts)
        
    def SetIndex(self, index):
        self.index = index
        self.indSelect.SetItems(self.index)

    def OnFromActText(self, event):
        if self.fromAct.ignoreEvtText:
            self.fromAct.ignoreEvtText = False
            return
        currentText = event.GetString()
        found = False
        for choice in self.acts:
            if choice.startswith(currentText):
                self.fromAct.ignoreEvtText = True
                self.fromAct.SetValue(choice)
                self.fromAct.SetInsertionPoint(len(currentText))
                self.fromAct.SetMark(len(currentText), len(choice))
                found = True
                break
        if not found:
            event.Skip()

    def OnFromActCombobox(self, event):
        self.fromAct.ignoreEvtText = True
        event.Skip()
        
    def OnFromActChar(self, event):
        if event.GetKeyCode() == 8:
            self.fromAct.ignoreEvtText = True
        event.Skip()
        
    def OnToActText(self, event):
        if self.toAct.ignoreEvtText:
            self.toAct.ignoreEvtText = False
            return
        currentText = event.GetString()
        found = False
        for choice in self.acts:
            if choice.startswith(currentText):
                self.toAct.ignoreEvtText = True
                self.toAct.SetValue(choice)
                self.toAct.SetInsertionPoint(len(currentText))
                self.toAct.SetMark(len(currentText), len(choice))
                found = True
                break
        if not found:
            event.Skip()

    def OnToActCombobox(self, event):
        self.toAct.ignoreEvtText = True
        event.Skip()
        
    def OnToActChar(self, event):
        if event.GetKeyCode() == 8:
            self.toAct.ignoreEvtText = True
        event.Skip()
