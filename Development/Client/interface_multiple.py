import wx
import time

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import *

class Interface(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title='RADiCal' , size=(650,350))
		self.parent = parent

		self.panel = wx.Panel(self)
		self.states = wx.StaticBox(self.panel, label='Speed multiple targets:', pos=(25, 100), size=(600, 200))

		self.targets = wx.StaticText(self.panel, wx.ID_ANY, label="Number of targets detected: ", pos=(110,30))
		font2 = wx.Font(24, wx.MODERN, wx.ITALIC, wx.BOLD)
		self.targets.SetFont(font2)

		#Inside the box
		self.pos1 = wx.StaticText(self.panel, label='Vehicle #1: -- km/h', pos=(40, 130))
		self.pos2 = wx.StaticText(self.panel, label='Vehicle #2: -- km/h', pos=(40, 200))
		self.pos3 = wx.StaticText(self.panel, label='Vehicle #3: -- km/h', pos=(40, 270))
		self.pos4 = wx.StaticText(self.panel, label='Vehicle #4: -- km/h', pos=(340, 130))
		self.pos5 = wx.StaticText(self.panel, label='Vehicle #5: -- km/h', pos=(340, 200))
		self.pos6 = wx.StaticText(self.panel, label='Vehicle #6: -- km/h', pos=(340, 270))

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

	def update_stats(self, v, targets):

		i = 1;
		self.targets.SetLabel("Number of targets detected: %.1f" %targets)

		for i in range(targets):

			if i == 1:
				self.pos1.SetLabel(" Vehicle #1: %.2f  km/h" %v[0])

			elif i == 2:
				self.pos2.SetLabel(" Vehicle #2: %.2f  km/h" %v[1])

			elif i == 3:
				self.pos3.SetLabel(" Vehicle #3: %.2f  km/h" %v[2])

			elif i == 4:
				self.pos4.SetLabel(" Vehicle #4: %.2f  km/h" %v[3])

			elif i == 5:
				self.pos5.SetLabel(" Vehicle #5: %.2f  km/h" %v[4])

			elif i == 6:
				self.pos6.SetLabel(" Vehicle #6: %.2f  km/h" %v[5])


if __name__ == "__main__":

	app = wx.App(False)
	i = Interface(None)
	i.Show(True)

	app.MainLoop()

