
import numpy as np
from scipy.signal import chebwin

WLEN = 4096				# Window length
H = WLEN/4				# Overlaping at the STFT
NFFT = 4096				# Number of samples to compute the FFT
Fs = 44100				# Hz Frequency Sampling
FLimitSpeed = 1600		# Hz Frequency limiting the region of interest
FLimitPedestrian = 200	# Hz Frequency limiting the region of interest for pedestrians
FLimitFlicker = 400		# Hz Frequency limit of the flicker noise
G = 20					# dB Gain from FLimitFlicker to 0 Hz
F_0 = 9.65e9			# Carrier Frequency
Kp = 0					# ped/Watts constant to estimate the number of pedestrians
Kv = 0					# veh/Watts constant to estimate the number of vehicles

h = 0					# m hight of the radar
d = 0
l = 0

def algorithm(x):
	"""
	Algorithm to compute from a vector containing the signal captured
	from the radar information of the street.
	Information computed:
	- Minimum speed seen from the cars
	- Maximum speed seen from the cars
	- Mean speed seen from the cars
	- Number of vehicles seen
	- Number of pedestrians seen
	"""

	if type(x) != np.ndarray:
		x = np.array(x)
	assert type(x) is np.ndarray, 'The input is not a vector'

	info = np.zeros((1,5)) 			# V_min, V_max, V_mean, N_veh, N_ped
	xlen = len(x)

	win = chebwin(WLEN, at=100)		# Attenuation 100dB

	# Initialize index and threshold
	indx = 0;
	threshold = 1e4;				# Lineal

	# Frequencies vector
	f = np.arange(NFFT / 2) / NFFT * Fs

	while indx + WLEN < xlen:

		xw = x[indx:(indx+WLEN)] * win
		xw = xw - np.mean(xw)

		X = np.abs(np.fft.fft(xw, NFFT))[:NFFT/2]
		X_2 = X[f[X<threshold]>FLimitFlicker]
		mn = np.mean(X_2)
		st = np.std(X_2)
		threshold = mn + 5 * st
		flat_threshold_dB = 20 * np.log10(threshold)

		ramp_threshold_dB = flat_threshold_dB - G / FLimitFlicker * (f - FLimitFlicker)
		threshold_dB = np.array([max(flat_threshold_dB, t) for t in ramp_threshold_dB])

		f_obs = f[f<FLimitSpeed]
		X = X[f<FLimitSpeed]
		XdB = 20 * np.log10(X)
		threshold_dB = threshold_dB[f<FLimitSpeed]

		# Compute the power from 0 to 200 Hz to stimate the average number of pedestrians
		power_ped = np.sum(X[f_obs<FLimitPedestrian])
		N_ped = Kp * power_ped

		# Compute the power from 200 Hz to 1.5 kHz to stimate the average number of vehicles
		power_veh = np.sum(X[f_obs>=FLimitPedestrian])
		N_veh = Kv * power_veh

		# Creation of PDF of velocities to estimate average speed of vehicles
		pdf = np.concatenate([np.zeros(len(f[f_obs<FLimitPedestrian])),X[f_obs>=FLimitPedestrian]])
		pdf = [max(pdf[i], threshold[i]) for i in range(len(pdf))]
		pdf = pdf - threshold
		pdf = pdf / np.sum(pdf)
		f_mean = np.sum(f_obs*pdf)
		v_mean = compute_speed(f_mean)

		# Finding peaks
		pks_pos = find_peaks(XdB, bandwidth = 10)
		pks_pos = pks_pos[XdB[pks_pos] > threshold_dB[pks_pos]]
		v = compute_speed(f_obs[f_obs[pks_pos]>FLimitPedestrian])

		# Determine the v_min and v_max
		v_min = max(min(v),0)
		v_max = max(max(v),0)

		# update indexes
		indx = indx + h

		# Gathering
		aux = [v_min, v_max, v_mean, N_veh, N_ped]
		info = np.concatenate(info, [aux])

	info = info[1:]
	final_info = np.concatenate([min(info[:, 0]), max(info[:, 1]), np.mean(info[:, 2:])]) 

	return final_info


def find_peaks(vector, threshold = None, bandwidth = 1):
	pos = []
	i = 0
	prev = [None] * bandwidth
	for x in vector[:-1]:
		isPeak = True

		if (i+bandwidth) < len(vector):
			after = vector[range(i+1, i+1+bandwidth)]
		else:
			after = np.concatenate([vector[i+1:], [None]*(bandwidth-(len(vector)-i-1))])
		
		for l in range(bandwidth):
			if (x < prev[l]) | (x < after[l]) | (x < threshold):
				isPeak = False
		if isPeak:		
			pos.append(i)
		prev[:-1] = prev[1:]
		prev[-1] = x
		i = i + 1
	return np.array(pos)



def compute_speed(freq):

	speed = freq * 3e8 / (2 * F_0) * 3.6		# km/h

	# transform speed
	return speed


if __name__ == '__main__':
	x = np.array(range(40))/4.0
	y = np.sin(x)
	print find_peaks(y)
	print find_peaks(y, bandwidth = 3)
	print find_peaks(y, bandwidth = 40)
	print find_peaks(y, threshold = 1)
	print find_peaks(y, threshold = 1, bandwidth = 40)	


