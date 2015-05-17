
from algorithm import algorithm
from capture import Capture
from connection import Connection
from numpy import *
import logging

RADAR_ID = 1
STREETS = [1, 2]
TIME = 30			# s seconds of the capture



# Init logger
logging.basicConfig(format='%(asctime)s %(message)s', filename = 'radar.log')

capture = Capture(logging.getLogger(run))
connection = Connection()

i = 0
while True:
	data = capture.record()
	info = algorithm(datas)
	info = concatenate(([STREET[i]], info, [TIME]))
	connection.send_capture(info)

	# Move radar with the servo motors
	
	i = (i+1) % len(STREETS)