
import protocol as p
import socket
import time
import numpy as np

"""
Connection class of the client
"""

HOST = '52.10.85.244'
#HOST = 'localhost'
#HOST = '192.168.2.1'
PORT = 30000
server_adress = (HOST, PORT)

# States of the States Machine
IDLE = 0
CONNECTED = 1
DISCONNECTED = 2
SUBSCRIBED = 3

class Connection(object):

	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect(server_adress)
		self.state = IDLE
		self.init_connection()

	def init_connection(self):
		self.socket.send(chr(p._CONNECT_CLIENT))
		self.state = CONNECTED
		print 'Connected'

	def disconnect(self):
		self.close_connection()

	def subscribe(self, i):
		self.socket.send(chr(p._SUBSCRIBE) + chr(i))
		self.state = SUBSCRIBED

	def unsubscribe(self):
		self.socket.send(chr(p._UNSUBSCRIBE))
		self.state = CONNECTED

	def close_connection(self):
		try:
			self.socket.send(chr(p._DISCONNECT_CLIENT))
			self.socket.shutdown(socket.SHUT_RDWR)
			self.socket.close()
			self.state = DISCONNECTED
			print 'Connection Closed'
		except Exception, e:
			raise e

	def receive(self):
		data = self.socket.recv(64)
		return data
		if data[0] == chr(p._DATA):
			return data[1:]

	def get_state(self):
		return self.state



if __name__ == '__main__':
	pi = Connection()
	time.sleep(2)
	pi.send_data(12.2)
	pi.disconnect()
