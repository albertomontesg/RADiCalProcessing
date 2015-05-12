
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import struct
import scipy.signal
from cPickle import load, dump

#SAVE_DIR = '/media/usb/RADiCal/test/test%d.pkl'

CHUNK = 512
FORMAT = pyaudio.paFloat32
CHANNELS = 1L
RATE = 44100
RECORD_SECONDS = 5
DEVICE_ID = 2
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
				channels=CHANNELS,
				rate=RATE,
				input=True,
				input_device_index=DEVICE_ID,
				frames_per_buffer=CHUNK)

def rec():
	print("* recording")

	frames = ''

	try:
		stream.start_stream()
		for i in range(500):
			data = stream.read(CHUNK)
			frames += data

			#print 'Capture:', i
		print("* done recording")
	finally:
		stream.stop_stream()
		stream.close()
		p.terminate()
	return np.fromstring(frames,np.float32)


def process(data):
	ft = 20*np.log10(np.abs(data))
	#peaks = scipy.signal.find_peaks_cwt(ft)
	print ft

def save(data, num):
	save_path = SAVE_DIR % num
	save_file = open(save_path, 'w')
	dump(data, save_file)

if __name__ == '__main__':
	data = rec()
	plt.figure()
	plt.plot(data)
	plt.savefig('figure1.png')
	plt.figure()
	plt.plot(20*np.log10(abs(np.fft.fft(data, 1024))))
	plt.savefig('figure2.png')