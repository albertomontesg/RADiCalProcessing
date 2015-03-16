import protocol as p
from threading import Thread
import socket
import numpy as np

HOST = '52.10.85.244'
PORT = 30000
server_adress = (HOST, PORT)

class Client(Thread):
	"""Worker Thread Class."""
	def __init__(self, interface):
		super(Client, self).__init__()
		self.interface = interface
		self.v = np.zeros((1,10))
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.s.connect(server_adress)
		except:
			pass

	def run(self):
		index = 0
		while True:
			try:
				data = self.s.recv(1024)
			except:
				self.s.close()
			
			targets = p.decode(bytearray(data))

			#Take the speed array

			print 'Speed recorded is:', speed, 'km/h'


			#Send to interface
			self.interface.update_stats(v, targets)

if __name__ == '__main__':
	c = Client(None)
	c.start()
