
from algorithm import *
from scipy.io import wavfile
from capture import Capture
from connection import Connection
from numpy import *
import logging
from threading import Thread


RADAR_ID = 1
STREETS = [1]
TIME = 30			# s seconds of the capture


# Init logger
# logging.basicConfig(format='%(asctime)s %(message)s', filename = 'radar.log')

if __name__ == '__main__':
	
	capture = Capture()
	connection = Connection()


	i = 0
	while True:
		data = capture.record(time = TIME)
		info = algorithm(datas)
		info = concatenate(([STREET[i]], info, [TIME]))
		connection.send_capture(info)

		# Move radar with the servo motors

		i = (i+1) % len(STREETS)



