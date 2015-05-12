
import protocol as p
import socket
import time

#HOST = '52.10.85.244'
HOST = 'localhost'
#HOST = '192.168.2.1'
PORT = 30000
server_adress = (HOST, PORT)

CONNECT_PI = 0x01
DISCONNECT_PI = 0x02
DATA = 0x07

speeds = [123.4, 34.3, 97.5, 45.6, 99.9]

class Connection(object):

	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect(server_adress)
		self.init_connection()

	def init_connection(self):
		self.socket.send(chr(CONNECT_PI))
		print 'Connected'

	def disconnect(self):
		self.close_connection()

	def close_connection(self):
		try:
			self.socket.send(chr(DISCONNECT_PI))
			self.socket.shutdown(socket.SHUT_RDWR)
			self.socket.close()
			print 'Connection Closed'
		except Exception, e:
			raise e

	def send_data(self, data):
		try:
			print 'Send data: ' + str(data)
			self.socket.send(chr(DATA)+p.code_1_information(data))
		except Exception, e:
			self.close_connection()
			raise e
		
if __name__ == '__main__':
	pi = Connection()
	time.sleep(2)
	pi.send_data(12.2)
	pi.disconnect()
