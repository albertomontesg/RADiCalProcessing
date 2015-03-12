import numpy as np
import wx
import matplotlib
import matplotlib.pyplot as plt

class Histogram(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title='Speed Histogram' , size=(650,350))
		self.parent = parent

		self.panel = wx.Panel(self)

		#v = [np.random.random_integers(30, 300, None)] * 100
		v = [50, 50 , 60, 70]
		f = [0.0] * 300
		x = np.arange(0, 300, 1)

		for i in range(len(v)):
			f[int(np.trunc(v[i]))] = f[int(np.trunc(v[i]))] + 1

		f_norm = f / np.sum(f)


		print "Creant..."

		hist = plt.bar(x, f_norm)

		print "Creat"
		
		plt.xlabel('Speed')
		plt.ylabel('Probability')
		plt.title('Histogram of Speed')
		plt.axis([0, 100, 0, 1])
		plt.grid(True)
		plt.show()

if __name__ == "__main__":

	app = wx.App(False)
	h = Histogram(None)
	h.Show(True)

	app.MainLoop()