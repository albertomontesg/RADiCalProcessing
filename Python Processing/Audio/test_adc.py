
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import struct
import scipy.signal
from cPickle import load, dump

SAVE_DIR = '/media/usb/RADiCal/test/test%d.pkl'

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1L
RATE = 44100
RECORD_SECONDS = 5
DEVICE_ID = 0
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
				channels=CHANNELS,
				rate=RATE,
				input=True,
				input_device_index=DEVICE_ID,
				frames_per_buffer=CHUNK)

def rec():
	# p = pyaudio.PyAudio()

	# stream = p.open(format=FORMAT,
	# 				channels=CHANNELS,
	# 				rate=RATE,
	# 				input=True,
	# 				input_device_index=DEVICE_ID,
	# 				frames_per_buffer=CHUNK)

	print("* recording")

	frames = []
	proces = np.array([])

	try:
		stream.start_stream()
		for i in range(1000):
			data = stream.read(CHUNK)
			frames.append(data)
			d = np.array(struct.unpack('h'*CHUNK, data))
			process(d)
			print 'Capture:', i
		print("* done recording")

		for f in frames:
			temp = struct.unpack('h'*CHUNK, f)
			proces = np.append(proces, np.array(temp))
	finally:
		stream.stop_stream()
		stream.close()
		p.terminate()
	return proces


def process(data):
	ft = 10*np.log10(np.abs(data))
	#peaks = scipy.signal.find_peaks_cwt(ft)
	print ft

def save(data, num):
	save_path = SAVE_DIR % num
	save_file = open(save_path, 'w')
	dump(data, save_file)

#data = np.array(frames)
#plt.plot(proces)
#plt.show()

if __name__ == '__main__':
	data = rec()