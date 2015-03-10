
import wx
import time

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('WXAgg')

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
		
		#Inside Speed Historial box
		self.pos1 = wx.StaticText(self.panel, label='-- km/h', pos=(40, 100))
		self.pos2 = wx.StaticText(self.panel, label='-- km/h', pos=(140, 100))
		self.pos3 = wx.StaticText(self.panel, label='-- km/h', pos=(240, 100))
		self.pos4 = wx.StaticText(self.panel, label='-- km/h', pos=(340, 100))
		self.pos5 = wx.StaticText(self.panel, label='-- km/h', pos=(440, 100))
		self.pos6 = wx.StaticText(self.panel, label='-- km/h', pos=(540, 100))

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

		index = 0

		for x in v:
			if x != 0:
				index += 1
		if index > 100:
			index = 100

		average = np.average(v[:index])
		min_s = np.min(v[:index])
		max_s = np.max(v)

		self.average.SetLabel("Average: %.1f km/h" %average)
		self.maxim.SetLabel("Maximum: %.1f km/h" %max_s)
		self.minim.SetLabel("Minimum: %.1f km/h" %min_s)


	"""def update_histogram(self, v, index):

		v_update = np.array(7)
		time = np.arange(0.00, 1.00, 100.00)
		start = 0
		end = 0

		if index < 7:
			v_update = v[0:6]
			t = time[0:6]

		else:
			start = index - 6
			end = start + 6
			v_update = v[start:end]
			t = time[start:end]"""

	def update_speedhist(self, v):
		
		v_update = v[:6]

		self.pos1.SetLabel(" %.2f  km/h" %v_update[0])
		self.pos2.SetLabel(" %.2f  km/h" %v_update[1])
		self.pos3.SetLabel(" %.2f  km/h" %v_update[2])
		self.pos4.SetLabel(" %.2f  km/h" %v_update[3])
		self.pos5.SetLabel(" %.2f  km/h" %v_update[4])
		self.pos6.SetLabel(" %.2f  km/h" %v_update[5])

	def update_speed(self, speed):
		self.speed.SetLabel("Actual Speed: %.1f" %speed)

class CanvasPanel(wx.Panel):
	def __init__(self, parent):
		Panel.__init__(self, parent)
		self.figure = Figure()
		self.axes = self.figure.add_subplot(111)
		self.canvas = FigureCanvas(self, -1, self.figure)
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
		self.SetSizer(self.sizer)
		self.Fit()

	def draw(self):
		t = arange(0.0, 3.0, 0.01)
		s = sin(2 * pi * t)
		self.axes.plot(t, s)


if __name__ == "__main__":
	app = wx.App(False)
	i = Interface(None)
	i.Show(True)

	app.MainLoop()


