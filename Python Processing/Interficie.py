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
		menuOpen = filemenu.Append(wx.ID_OPEN, "Open", "Open a file")
		filemenu.AppendSeparator()
		menuAbout = filemenu.Append(102, "About"," Information about this program")
		filemenu.AppendSeparator()
		menuExit = filemenu.Append(103,"Exit"," Terminate the program")

		menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
		self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

		# Creamos los eventos
		self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
		 
		self.Show(True)
   
	# Definimos los metodos de los eventos

	def EvtText(self, event):
		self.logger.AppendText('Evento de texto: %sn' % event.GetString)

	def EvtChar(self, event):
		self.logger.AppendText('Evento de caracter: %dn' % event.GetKeyCode())
		event.Skip()

	def OnAbout(self,e):
		# Creamos una ventana de dialogo con un boton de ok. wx.OK es una ID estandard de wxWidgets.
		dlg = wx.MessageDialog( self, "It is a doppler radar implemented by students of ETSETB", "About RADiCal", wx.OK)
		dlg.ShowModal() # La mostramos
		dlg.Destroy() # Finalmente la destruimos

	def OnExit(self,e):
		self.Close(True)  # Cerramos el frame
		
	def OnOpen(self,e):
		# Podemos crear un evento extra para abrir un fichero de texto
		"""Abrir un fichero"""
		self.dirname = ''
		# Abrimos una ventana de dialogo de fichero para seleccionar algun fichero
		dlg = wx.FileDialog(self, "Elige un fichero", self.dirname, "", "*.*", wx.OPEN)
		# Si se selecciona alguno => OK
		if dlg.ShowModal() == wx.ID_OK: 
			self.filename = dlg.GetFilename()   # Guardamos el nombre del fichero
			self.dirname = dlg.GetDirectory()   # Y el directorio
			
			# Abrimos el fichero en modo lectura
			f = open(os.path.join(self.dirname, self.filename), 'r')
			# Y con setValue pasamos el fichero al control de texto
			self.control.SetValue(f.read()) 
			f.close()   # Lo cerramos
		dlg.Destroy()   # Finalmente destruimos la ventana de dialogo

def Show():
	app = wx.App(False)
	MainWindow(None, "RADiCal")
	app.MainLoop()

if __name__ == "__main__":
	Show()
