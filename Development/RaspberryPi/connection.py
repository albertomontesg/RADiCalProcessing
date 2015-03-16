
import protocol as p
import socket
import time

#HOST = '52.10.85.244'
HOST = 'localhost'
#HOST = '192.168.2.1'
PORT = 30000
server_adress = (HOST, PORT)

speeds = [123.4, 34.3, 97.5, 45.6, 99.9]

class Connection(object):

	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect(server_adress)

	def send_speed(self, speed):
		self.socket.sendall(p.code_1_information(speed))

	def get_value(self, i):
		## get value from the serial
		## return value as integer
		
		print 'Send:', speeds[i%5]
		return speeds[i%5]

	def get_from_arduino(self):
		pass

	def single_vehicle(self):

		while True:
			speed = get_value()
			try:
				s.sendall(p.code_1_information(speed))
			except:
				s.close()
			time.sleep(.5)

if __name__ == '__main__':
	pi = Connection()
	# auth = bytearray(2)
	# print int(auth[0])
	# s.sendall(auth)
	i = 0
	while True:
		speed = pi.get_value(i)
		pi.socket.sendall(p.code_1_information(speed))
		time.sleep(.5)
		i += 1
