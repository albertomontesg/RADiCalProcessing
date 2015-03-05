import wx, os

class MainWindow(wx.Frame):
	""" Una clase personalizada de frame """
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title='RADiCal' , size=(650,400))
		#self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		self.parent = parent
		
		panelB = wx.Panel(self)
		wx.StaticBox(panelB, label='Some states:', pos=(10, 150), size=(300, 200))
		wx.StaticBox(panelB, label='Histogram:', pos=(345, 150), size=(300, 200))

		self.speed = wx.StaticText(panelB, label="Actual Speed: ", pos=(20,30))

		#Inside Some States box:
		self.average = wx.StaticText(panelB, label="Average: ", pos=(30, 180))
		self.maxim = wx.StaticText(panelB, label="Maximum: ", pos=(30, 210))
		self.aminim = wx.StaticText(panelB, label="Minimum: ", pos=(30, 240))
		
		self.CreateStatusBar() 

		menuBar = wx.MenuBar()

		filemenu = wx.Menu()
		menuAbout = filemenu.Append(102, "About"," Information about this program")
		filemenu.AppendSeparator()
		menuExit = filemenu.Append(103,"Exit"," Terminate the program")

		menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
		self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

		# Creamos los eventos
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
   
	# Definimos los metodos de los eventos
	def OnAbout(self,e):
		# Creamos una ventana de dialogo con un boton de ok. wx.OK es una ID estandard de wxWidgets.
		dlg = wx.MessageDialog( self, "It is a doppler radar implemented by students of ETSETB", "About RADiCal", wx.OK)
		dlg.ShowModal() # La mostramos
		dlg.Destroy() # Finalmente la destruimos

	def OnExit(self,e):
		self.Close(True)  # Cerramos el frame
		

def Show():
	app = wx.App(False)
	MainWindow(None, "RADiCal")
	app.MainLoop()

if __name__ == "__main__":
	Show()
