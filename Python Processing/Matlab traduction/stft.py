from numpy import *
from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt

def stft(x, wlen, h, nfft, fs):

	#Represent x as column-vector if it is not
	if x.shape[1] > 1:
		x.conj().transpose()

	#Length of the signal
	xlen = x.size

	#Chebyschev window
	win = scipy.signal.chebwin(xlen, 1.0)

	#Form the stft matrix
	rown = ceil((1+nfft)/2)				#calculate the total number of rows
	coln = 1+fix((xlen-wlen)/h)			#calculate the total number of columns
	stft = zeros(rown, coln)			#form the stft matrix

	#Initialize the indexes
	indx = 0
	col = 1

	#Perform STFT
	threshold = 1000000;

	while (indx+wlen) in range(xlen):

		#windowing
		xw = [i * win for i in x(indx+1 : indx+wlen)]

		#FFT
		X = fft.fft(xw, nfft)

		#Plot
		K = X.size

		f_plot = (1 : floor(K/2)) * fs / K
		f_plot = f_plot(f_plot < 7000)
		fft_x = abs (X(1:f_plot.size ,1))
		FFT = 20*log10(fft_x)


		pos = fft_x<threshold
		mn = mean(fft_x(pos))
		st = std(fft_x(pos))
		threshold = (mn + 5*st)

		#Aqui va el plot
		plt.plot(f_plot,fft_x,f_plot, threshold*ones(length(f_plot)),'-r')


		#locs = locs(pks > threshold)
    	#pks = pks(pks > threshold)

		indx = indx + h
		col = col + 1

	t = (wlen/2:h:xlen-wlen/2-1)/fs
	f = (0:rown-1)*fs/nfft

