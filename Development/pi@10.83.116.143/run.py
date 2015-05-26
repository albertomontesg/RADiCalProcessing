
from algorithm import *
from scipy.io import wavfile
from capture import Capture
from connection import Connection
from numpy import *
import logging
from threading import Thread
from time import time
from serial_connection import SerialConnection


RADAR_ID = 1
STREETS = [1, 2, 3]
TIME = 20			# s seconds of the capture


# Init logger
# logging.basicConfig(format='%(asctime)s %(message)s', filename = 'radar.log')

if __name__ == '__main__':
	
	capture = Capture()
	connection = Connection()
	motor = SerialConnection()

	i = 0
	while True:
		# try:
		motor.move(i)
		time.sleep(1)
		data = capture.record(time = TIME)
		start = time()
		info = algorithm(downsampling(data))
		stop = time()
		print 'Algorithm expend: ', (stop-start), ' seconds'
		info = concatenate((RADAR_ID[i], info, [TIME]))
		print 'Algorithm info: ', info
		connection.send_capture(info)

		# Move radar with the servo motors

		i = (i+1) % len(STREETS)
		# except Exception, e:
		# 	capture.close()
		# 	connection.disconnect()
		# 	capture = Capture()
		# 	connection = Connection()
		# 	raise e
		# 	motor.close()