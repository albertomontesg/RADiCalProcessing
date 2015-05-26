import pyaudio
from numpy import *

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1L
RATE = 44100
DEVICE_ID = 2

class Capture(object):
	"""docstring for Capture"""
	def __init__(self):
		super(Capture, self).__init__()
		self.audio = pyaudio.PyAudio()

	def record(self, time = 30):
		self.stream = self.audio.open(format=FORMAT,
							channels=CHANNELS,
							rate=RATE,
							input=True,
							input_device_index=DEVICE_ID,
							frames_per_buffer=CHUNK)
		print "Start Recording"

		frames = ''
		for i in range(0, int(RATE * time / CHUNK)):
			data = self.stream.read(CHUNK)
			frames += data

		print "Stop Recording"

		self.stream.stop_stream()
		self.stream.close()
		signal = fromstring(frames, dtype = int16)
		signal = float16(signal) / 2**15
		return signal

	def close(self):
		self.stream.stop_stream()
		self.stream.close()
		self.audio.terminate()

if __name__ == '__main__':
	c = Capture()
	data = c.record(time = 5)
	print data
	print len(data)