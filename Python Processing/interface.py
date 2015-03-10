
import wx
import time

import numpy as np
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

class Interface(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title='RADiCal' , size=(650,400))
		self.parent = parent

		self.panel = wx.Panel(self)
		self.states = wx.StaticBox(self.panel, label='Some states:', pos=(10, 150), size=(300, 140))
		self.hist = wx.StaticBox(self.panel, label='Histogram:', pos=(345, 150), size=(300, 200))
		self.speedhist = wx.StaticBox(self.panel, label='Speed Historial:', pos=(10, 80), size=(630, 50))


		self.speed = wx.StaticText(self.panel, wx.ID_ANY, label="Actual Speed: ", pos=(150,30))
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

		"""#Inside Speed Historial box
		self.pos1 = wx.StaticText(self.panel, label='-- km/h', pos=(25, 100))
		self.pos2 = wx.StaticText(self.panel, label='-- km/h', pos=(115, 100))
		self.pos3 = wx.StaticText(self.panel, label='-- km/h', pos=(205, 100))
		self.pos4 = wx.StaticText(self.panel, label='-- km/h', pos=(295, 100))
		self.pos5 = wx.StaticText(self.panel, label='-- km/h', pos=(385, 100))
		self.pos6 = wx.StaticText(self.panel, label='-- km/h', pos=(475, 100))
		self.pos7 = wx.StaticText(self.panel, label='-- km/h', pos=(565, 100))"""
		
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


	def update_stats(self, v):
		average = np.average(v)
		min_s = np.min(v)
		max_s = np.max(v)

		self.average.SetLabel("Average: %.1f km/h" %average)
		self.maxim.SetLabel("Maximum: %.1f km/h" %max_s)
		self.minim.SetLabel("Minimum: %.1f km/h" %min_s)


	# def update_histogram(speeds):

	#def update_speedhist(self, v):



	def update_speed(self, speed):
		self.speed.SetLabel("Actual Speed: %.1f km/h" %speed)

if __name__ == "__main__":
	app = wx.App(False)

	app.MainLoop()
