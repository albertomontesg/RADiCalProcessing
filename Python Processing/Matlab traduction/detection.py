from numpy import *
from scipy import signal
from scipy.io import wavfile
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt

wlen = 512			# Window length
h = wlen/2			# Overlaping
nfft = 1024			# FFT samples
fs = 44100 			# Frequency Sampling
fobs = 7000 		# Search peaks until 7kHz
global threshold	# Initialize threshold

debug = False		# Debug option

def stft(x):

	if debug:
		plt.plot(x)
		plt.show()

	#Length of the signal
	xlen = x.size
	# Construction of the Chebyschev window
	win = signal.chebwin(wlen, 100)

	#Form the stft matrix
	rown = ceil((1+nfft)/2)				#calculate the total number of rows
	coln = 1+fix((xlen-wlen)/h)			#calculate the total number of columns
	stft = zeros(rown, coln)			#form the stft matrix

	#Initialize the indexes
	indx = 0
	col = 1

	#Perform STFT
	global threshold 
	threshold = 1e7;

	record = zeros(coln)
	i = 0

	# For every window samples detect the peaks
	while (indx+wlen) < xlen:

		# Windowing the signal
		xw = win * x[indx:indx+wlen]
		freq, pwr = detection(xw)

		record[i] = len(freq)

		# Updating indexes
		indx = indx + h
		i = i + 1

	plt.plot(record)
	plt.show()

	col = col + 1

	t = arange(wlen/2,xlen-wlen/2-1, h)/fs
	f = arange(0,rown-1,1)*fs/nfft

def detection(x):
	global threshold
	if debug:
		print 'threshold:', threshold

	freq = []
	pwr = []

	X = fft(x, nfft)
	XX = 10*log10(abs(X))[range(int(nfft*fobs/fs))]
	f = array(range(nfft), dtype = float32)/nfft*fs

	if False:
		plt.plot(f, 10*log10(abs(X)))
		plt.show()

	#pos = signal.find_peaks_cwt(XX, arange(1,10))
	pos = find_peaks(XX)
	if len(pos) > 0:
		pks = XX[pos]

		val_pks = pks[where(pks<threshold)]
		mhu = mean(val_pks)
		sigma = std(val_pks)
		threshold = mhu + 4 * sigma

		if debug:
			print 'pos', pos
			print 'f', f[pos]
			print 'pks', pks
			print 'val_pks', val_pks
			print 'mhu', mhu, 'sigma', sigma

		locs = pos[where(pks > threshold)]
		freq = f[locs]
		pwr = XX[locs]

		if debug:
			print 'locs', locs
			print 'freq', freq
			print 'pwr', pwr
			print 'threshold', threshold
			plt.plot(f[:len(XX)], XX, 'b')
			plt.plot(freq, pwr, 'ro')
			plt.show()

		if debug:
			# Pause
			raw_input()

	return freq, pwr

def find_peaks(vector, threshold = None):
	pos = []
	i = 1
	prev = vector[0]
	for x in vector[1:-1]:
		after = vector[i+1]
		if (x > prev) & (x > after) & (x > threshold):
			pos.append(i)
		prev = x
		i = i + 1
	return array(pos)


if __name__ == '__main__':
	i, x = wavfile.read('sample10.wav')
	x = x - mean(x)
	stft(x[:])