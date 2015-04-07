from numpy import *
from scipy import signal
from scipy.io import wavfile
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt

def stft( wlen, h, nfft, fs):

	i, x = wavfile.read('prova1.wav')

	#Represent x as column-vector if it is not
	#if x.shape[1] > 1:
	#	x.conj().transpose()

	#Length of the signal
	xlen = x.size

	#Chebyschev window
	win = signal.chebwin(wlen, 1.0)

	#Form the stft matrix
	rown = ceil((1+nfft)/2)				#calculate the total number of rows
	coln = 1+fix((xlen-wlen)/h)			#calculate the total number of columns
	stft = zeros(rown, coln)			#form the stft matrix

	#Initialize the indexes
	indx = 0
	col = 1

	#Perform STFT
	threshold = 1000000000;

	#h1, = plt.plot([], [])

	#while (indx+wlen) in range(xlen):

	#windowing
	xw = [i * win for i in x[indx+1 : indx+wlen]]

	#FFT
	X = fft(xw, nfft)

	#Plot
	K = X.size

	print('fft feta')

	f_plot = arange(1 ,floor(K/2), 1) * fs / K
	f_plot = (f_plot < 7000).nonzero()
	f_plot1 = list(f_plot)
	fft_x = abs(X[:len(f_plot1)])
	FFT = 20*log10(fft_x)

	print('densitat espectral calculada.')

	pos = 0
	index = 0

	for i in range(len(fft_x)):
		print (fft_x[i])
		print (fft_x)
		if(fft_x[i] < threshold).any():
			pos = append(pos, i)
			print(i)

	print(pos)

	mn = mean(fft_x[pos])
	st = std(fft_x[pos])
	threshold = (mn + 5*st)

	print('threshold calculat')

	#Aqui va el plot
	#plt.plot(f_plot1,fft_x,f_plot1, threshold*ones(len(f_plot)), char('-r'))

	#FindPeaks
	#pks, locs = findpeaks(fft_x, 'MinPeakHeight', threshold)
	#pks = signal.find_peaks_cwt(fft_x, threshold)

	#locs = (locs>threshold).nonzero()
	#pks = (pks > threshold).nonzero()

	indx = indx + h
	col = col + 1

	t = arange(wlen/2,xlen-wlen/2-1, h)/fs
	f = arange(0,rown-1,1)*fs/nfft

