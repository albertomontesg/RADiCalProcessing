from interface import Interface
import wx
from threading import Thread
from time import sleep
from radar import Radar
import numpy as np
from client import Client


class CustomThread(Thread):
	"""Worker Thread Class."""
	def __init__(self, interface):
		"""Init Worker Thread Class."""
		Thread.__init__(self)
		#self._notify_window = notify_window
		self.interface = interface
		self._want_abort = 0
		# This starts the thread running on creation, but you could
		# also make the GUI thread responsible for calling this

	def run(self):
		"""Run Worker Thread."""
		# This is the code executing in the new thread. Simulation of
		# a long process (well, 10s here) as a simple loop - you will
		# need to structure your processing so that you periodically
		# peek at the abort variable
		self.interface.Show(True)
		i.Show(True)
		rd = Radar(object)

		high = rd.setHeigh()
		lenght = rd.setLenght()
		distance = rd.setDistance()

		index = 0

		fd = [300.0, 5000.0, 4400.0, 2300.0, 700.0, 3021.0, 425.0, 742.0, 1506.0, 1002.0, 5302.0, 2890.0, 3876.0]
		self.v =[min(fd)] * len(fd)
		

		for index in range(len(fd)):

			self.v[index] = rd.processing(fd[index], high, lenght, distance)

			sleep(1)
			i.update_speed(self.v[index])
			i.update_stats(self.v, index)
			i.update_speedhist(self.v, index)
			#i.update_histogram(self.v, index)

		if self._want_abort:
			# Use a result of None to acknowledge the abort (of
			# course you can use whatever you'd like or even
			# a separate event type)
			wx.PostEvent(self._notify_window, ResultEvent(None))
			return


	def abort(self):
		"""abort worker thread."""
		# Method for use by main thread to signal an abort
		self._want_abort = 1

if __name__ == "__main__":
#inizialitzem interface
# inicilitzem classe radar
# preguntem dades
# fem un show de la interface
# loop mostrant dades
	

	app = wx.App(False)
	i = Interface(None)
	i.Show(True)

	client = Client(i)
	client.start()

	app.MainLoop()
