
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
		wx.StaticBox(self.panel, label='Some states:', pos=(10, 150), size=(300, 200))
		wx.StaticBox(self.panel, label='Histogram:', pos=(345, 150), size=(300, 200))

		self.speed = wx.StaticText(self.panel, label="Actual Speed: ", pos=(20,30))

		#Inside Some States box:
		self.average = wx.StaticText(self.panel, label="Average: ", pos=(30, 180))
		self.maxim = wx.StaticText(self.panel, label="Maximum: ", pos=(30, 210))
		self.aminim = wx.StaticText(self.panel, label="Minimum: ", pos=(30, 240))
		
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


	# def update_stats(aver, min, max):


	# def update_histogram(speeds):



	def update_speed(self, speed):
		self.speed.SetLabel("Actual Speed: %.1f"%speed)
		self.panel.Layout()

if __name__ == "__main__":
	app = wx.App(False)
	i = Interface(None)
	i.Show(True)


	speed = 1.0
	while True:
		time.sleep(1)
		speed += 1
		i.update_speed(speed)
		print speed
