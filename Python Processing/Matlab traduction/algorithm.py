
from numpy import * 
from scipy.io import wavfile
from scipy.signal import chebwin

WLEN = 4096				# Window length
H = WLEN/4				# Overlaping at the STFT
NFFT = 1024				# Number of samples to compute the FFT
Fs = 44100.0			# Hz Frequency Sampling
FLimitSpeed = 1600.0	# Hz Frequency limiting the region of interest
FLimitPedestrian = 200.0# Hz Frequency limiting the region of interest for pedestrians
FLimitFlicker = 400.0	# Hz Frequency limit of the flicker noise
G = 20.0				# dB Gain from FLimitFlicker to 0 Hz
F_0 = 9.65e9			# Carrier Frequency
Kp = 1.0				# ped/Watts constant to estimate the number of pedestrians
Kv = 1.0				# veh/Watts constant to estimate the number of vehicles

h = 0.0					# m hight of the radar
d = 0.0					# m perpendicular distance to the road
l = 1.0					# m length from the projaction of the radar to the street to the 
						# spot of the antena beam
cosTheta = l / sqrt(l**2+h**2+d**2)

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

	if type(x) != ndarray:
		x = array(x)
	assert type(x) is ndarray, 'The input is not a vector'

	info = zeros((1,5)) 			# V_min, V_max, V_mean, N_veh, N_ped
	xlen = len(x)

	win = chebwin(WLEN, at=100)		# Attenuation 100dB

	# Initialize index and threshold
	indx = 0
	threshold = 1e4					# Lineal

	# Frequencies vector
	f = arange(NFFT / 2) * Fs / NFFT

	while indx + WLEN < xlen:
		# print indx

		xw = x[indx:(indx+WLEN)] * win
		xw = xw - mean(xw)

		X = abs(fft.fft(xw, NFFT))[:NFFT/2]
		X_2 = X[f[X<threshold]>FLimitFlicker]
		mn = mean(X_2)
		st = std(X_2)
		threshold = mn + 5 * st
		flat_threshold_dB = 20 * log10(threshold)

		ramp_threshold_dB = flat_threshold_dB - (f - FLimitFlicker) * G / FLimitFlicker
		threshold_dB = array([max(flat_threshold_dB, t) for t in ramp_threshold_dB])

		f_obs = f[f<FLimitSpeed]
		X = X[f<FLimitSpeed]
		XdB = 20 * log10(X)
		threshold_dB = threshold_dB[f<FLimitSpeed]

		# Compute the power from 0 to 200 Hz to stimate the average number of pedestrians
		power_ped = sum(X[f_obs<FLimitPedestrian])
		N_ped = Kp * power_ped

		# Compute the power from 200 Hz to 1.5 kHz to stimate the average number of vehicles
		power_veh = sum(X[f_obs>=FLimitPedestrian])
		N_veh = Kv * power_veh

		# Creation of PDF of velocities to estimate average speed of vehicles
		pdf = concatenate([zeros(len(f[f_obs<FLimitPedestrian])),X[f_obs>=FLimitPedestrian]])
		# for j in range(len(pdf)):
		# 	pdf[j] = max(pdf[j], threshold[j])
		pdf = [max(pdf[j], threshold) for j in range(len(pdf))]
		pdf = pdf - threshold
		if sum(pdf) != 0:
			pdf = pdf / sum(pdf)
		f_mean = sum(f_obs*pdf)
		v_mean = compute_speed(f_mean)

		# Finding peaks
		pks_pos = find_peaks(XdB, bandwidth = 5)
		pks_pos = pks_pos[XdB[pks_pos] > threshold_dB[pks_pos]]
		f_pks = f_obs[pks_pos]
		v = compute_speed(f_pks[f_pks>FLimitPedestrian])

		# Determine the v_min and v_max
		v_min, v_max = 0, 0
		if len(v) > 0:
			v_min = min(v)
			v_max = max(v)

		# update indexes
		indx = indx + H

		# Gathering
		aux = [v_min, v_max, v_mean, N_veh, N_ped]
		info = concatenate([info, [aux]], 0)

	info = info[1:]
	v_min = min(info[info[:,0] != 0, 0])
	v_max = max(info[info[:,1] != 0, 1])
	me = mean(info[info[:,2] != 0, 2])
	nums = sum(info[:, 3:], 0)
	print v_min, v_max, me, nums
	final_info = concatenate(([v_min], [v_max], [me], nums))

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
			after = concatenate([vector[i+1:], [None]*(bandwidth-(len(vector)-i-1))])
		
		for l in range(bandwidth):
			if (x < prev[l]) | (x < after[l]) | (x < threshold):
				isPeak = False
		if isPeak:		
			pos.append(i)
		prev[:-1] = prev[1:]
		prev[-1] = x
		i = i + 1
	return array(pos)


def compute_speed(freq):

	speed = freq * 3e8 / (2 * F_0) * 3.6		# km/h
	speed = speed / cosTheta
	# transform speed
	return speed

def frequency_divider(x, divider = 1):
	return x[(array(range(len(x))) % divider) == 0]


if __name__ == '__main__':	

	i, x = wavfile.read('testPython/sample9.wav')
	print "Read wav"
	x = array(x, dtype=float32)/2**15
	print len(x)
	#x = frequency_divider(x, 8)
	print len(x)
	data = algorithm(x)
	print data
