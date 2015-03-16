
import protocol as p
from threading import Thread
import socket
import numpy as np

#HOST = '52.10.85.244'
HOST = 'localhost'
PORT = 30000
server_adress = (HOST, PORT)

EPSILON = 0.0

class TCPClient():

	def __init__(self, host, port, retryAttempts = 10):
		self.host = host
		self.port = port
		self.retryAttempts = retryAttempts
		self.socket = None

	def connect(self, attemp = 0):
		if attemp < self.retryAttempts:
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			try:
				self.socket.connect((self.host, self.port))
				auth = bytearray(1)
				self.socket.sendall(auth)
			except:
				self.connect(attemp + 1)


	def disconnect(self):
		self.socket.close()
		self.socket = None

	def readData(self):
		data = self.socket.recv(1024)

		return data

class Client(Thread):
	"""Worker Thread Class."""
	def __init__(self, interface, histogram):
		super(Client, self).__init__()
		self.interface = interface
		self.histogram = histogram
		self.v = np.zeros((1,100))
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.s.connect(server_adress)
		except:
			pass

	def run(self):
		index = 0
		last_speed = 0

		while True:
			try:
				data = self.s.recv(1024)

				speed = p.decode(bytearray(data))

				print 'Speed recorded is:', speed, 'km/h'
				#Send to interface
			except:
				self.s.close()

			speed = p.decode(bytearray(data))

			print 'Speed recorded is:', speed, 'km/h'

			if (speed > (last_speed + EPSILON)) | (speed < last_speed - EPSILON):
				self.v = np.append(speed, self.v)
				self.v = self.v[:100]


			index = index + 1

			#Send to interface
			self.interface.update_speed(speed)
			self.interface.update_stats(self.v, index)
			self.interface.update_speedhist(self.v)
			#self.histogram.update_hist(self.v, index)
			
			last_speed = speed


if __name__ == '__main__':
	c = Client(None)
	c.start()
