
import protocol as p
from threading import Thread
import socket

HOST = '52.10.85.244'
PORT = 30000
server_adress = (HOST, PORT)

class Client(Thread):
	"""Worker Thread Class."""
	def __init__(self, interface):
		super(Client, self).__init__()
		self.interface = interface
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.s.connect(server_adress)
		except:
			pass

	def run(self):
		while True:
			try:
				data = self.s.recv(1024)
			except:
				self.s.close()
			speed = p.decode(bytearray(data))

			print 'Speed recorded is:', speed, 'km/h'
			#Send to interface

if __name__ == '__main__':
	c = Client(None)
	c.start()
