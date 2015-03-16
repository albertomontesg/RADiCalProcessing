
from serial_connection import SerialConnection
from connection import Connection
from radar import Radar

SPEED_THRESHOLD = 0.0

if __name__ == "__main__":
	c = Connection()
	sc = SerialConnection()

	# Inicialize Radar
	radar = Radar()
	radar.setHeight()
	radar.setLength()
	radar.setDistance()

	while True:
		f = sc.get_data()	# Blocking method
		speed = radar.processing(f)
		if speed > SPEED_THRESHOLD:	# Greater than 2 km/h
			c.send_speed(speed)

	sc.close()
