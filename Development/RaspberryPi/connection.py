
import protocol as p
import socket
import time
import numpy as np

HOST = '52.10.85.244'
#HOST = 'localhost'
#HOST = '192.168.2.1'
PORT = 30000
server_adress = (HOST, PORT)



# States of the States Machine
IDLE = 0
CONNECTED = 1
DISCONNECTED = 2

i = [1, 1, 1, 1, 1, 1]
mi = [23.13, 12.34, 10.5, 9.9, 12.6, 14.0]
ma = [43.13, 32.34, 30.5, 29.9, 32.6, 34.0]
mean = [33.13, 22.34, 20.5, 19.9, 22.6, 24.0]
num = [100, 123, 89, 154, 98, 112]
ped = [40, 15, 23, 18, 23, 31]
time = [30]*6

class Connection(object):

	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect(server_adress)
		self.state = IDLE
		self.init_connection()

	def init_connection(self):
		self.socket.send(chr(p._CONNECT_PI))
		self.state = CONNECTED
		print 'Connected'

	def disconnect(self):
		self.close_connection()

	def close_connection(self):
		try:
			self.socket.send(chr(p._DISCONNECT_PI))
			self.socket.shutdown(socket.SHUT_RDWR)
			self.socket.close()
			self.state = DISCONNECTED
			print 'Connection Closed'
		except Exception, e:
			raise e

	def send_data(self, data):
		try:
			print 'Send data: ' + str(data)
			self.socket.send(chr(p._DATA)+data)
		except Exception, e:
			self.close_connection()
			raise e

	def get_state(self):
		return self.state
	
	def get_samples(self, pos):
		j = pos%6
		return p.code_information(i[j], mi[j], ma[j], mean[j], num[j], ped[j], time[j])



if __name__ == '__main__':
	pi = Connection()
	time.sleep(2)
	pi.send_data(12.2)
	pi.disconnect()
