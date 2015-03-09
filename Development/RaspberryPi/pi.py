
import protocol as p
import socket
import time

HOST = '52.10.85.244'
PORT = 30000
server_adress = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

speeds = [123.4, 34.3, 97.5, 45.6, 99.9]

def get_value(i):
	## get value from the serial
	## return value as integer
	
	print 'Send:', speeds[i%5]
	return speeds[i%5]


def single_vehicle():

	while True:
		speed = get_value()
		try:
			s.sendall(p.code_1_information(speed))
		except:
			s.close()
		time.sleep(.5)

if __name__ == '__main__':
	s.connect(server_adress)
	i = 0
	while True:
		speed = get_value(i)
		s.sendall(p.code_1_information(speed))
		time.sleep(.5)
		i += 1
