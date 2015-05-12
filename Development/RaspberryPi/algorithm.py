
import numpy as np
from scipy.signal import chebwin

WLEN = 4096
H = WLEN/4
NFFT = 4096
Fs = 44100
FLimitSpeed = 16000		# Hz Frequency limiting the region of interest
FLimitPedestrian = 200	# Hz Frequency limiting the region of interest for pedestrians
FLimitFlicker = 400		# Hz Frequency limit of the flicker noise
G = 20					# dB Gain from FLimitFlicker to 0 Hz
F_0 = 9.65e9			# Carrier Frequency



def algorithm(x):
	assert type(x) is type(nparray) 

	info = np.zeros(1,5) # V_min, V_max, V_mean, N_veh, N_ped
	xlen = len(x)

	win = chebwin(WLEN, at=100)		# Attenuation 100dB

	# Initialize index and threshold
	indx = 0;
	col = 1;
	threshold = 1e4;	# Lineal

	# Frequencies vector
	f = np.arange(NFFT/2)/NFFT*Fs

	while indx + WLEN < xlen:

		xw = x[indx:(indx+WLEN)] * win
		xw = xw - np.mean(xw)

		X = np.abs(np.fft.fft(xw, NFFT))
		X_2 = X[np.where(f[np.where(fft_X<threshold)]>FLimitFlicker)]
		mn = np.mean(X_2)
		st = np.std(X_2)
		threshold = mn + 5 * st
		flat_threshold_dB = 20*np.log10(threshold)

		ramp_threshold_dB = flat_threshold_dB - G/FLimitFlicker*(f-FLimitFlicker)
		threshold_dB = max(ramp_threshold_dB, np.ones(len(f))*flat_threshold_dB)