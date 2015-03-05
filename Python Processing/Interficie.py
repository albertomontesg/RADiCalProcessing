import wx, os

class MainWindow(wx.Frame):
	""" Una clase personalizada de frame """
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title='RADiCal' , size=(650,400))
		self.parent = parent
		
		self.panel = wx.Panel(self)
		wx.StaticBox(self.panel, label='Some states:', pos=(10, 150), size=(300, 140))
		wx.StaticBox(self.panel, label='Histogram:', pos=(345, 150), size=(300, 200))
		wx.StaticBox(self.panel, label='Speed Historial:', pos=(10, 80), size=(630, 50))

		self.speed = wx.StaticText(self.panel, label="Actual Speed: ", pos=(150,30))
		font2 = wx.Font(24, wx.MODERN, wx.ITALIC, wx.BOLD)
		self.speed.SetFont(font2)

		#Inside Some States box:
		self.average = wx.StaticText(self.panel, label="Average: ", pos=(30, 180))
		self.maxim = wx.StaticText(self.panel, label="Maximum: ", pos=(30, 210))
		self.minim = wx.StaticText(self.panel, label="Minimum: ", pos=(30, 240))
		font3 = wx.Font(15, wx.NORMAL, wx.ITALIC, wx.NORMAL)
		self.average.SetFont(font3)
		self.maxim.SetFont(font3)
		self.minim.SetFont(font3)
		
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
	frame = MainWindow(None)
	frame.Show(True)
	app.MainLoop()

if __name__ == "__main__":
	Show()
