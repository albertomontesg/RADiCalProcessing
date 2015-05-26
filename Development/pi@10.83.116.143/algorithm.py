
from numpy import * 
from scipy.io import wavfile
from scipy.signal import chebwin
from time import time
import filter

global Fs

WLEN = 4096					# Window length
DOWNSAMPLING = 8			# Take une sample for each 8 to reduce the computation
H = 0 # WLEN/4				# Overlaping at the STFT
NFFT = 512					# Number of samples to compute the FFT
Fs = 44100.0				# Hz Frequency Sampling
FLimitSpeed = 1600.0		# Hz Frequency limiting the region of interest
FLimitPedestrian = 200.0	# Hz Frequency limiting the region of interest for 
							# pedestrians
FLimitFlicker = 400.0		# Hz Frequency limit of the flicker noise
G = 20.0					# dB Gain from FLimitFlicker to 0 Hz
SNRmin = 10					# dB SNR min for detect the speed of the vehicles.
F_0 = 9.65e9				# Carrier Frequency
Kp = 1.0					# ped/Watts constant to estimate the number of pedestrians
Kv = 1.0					# veh/Watts constant to estimate the number of vehicles

h = 0.0						# m hight of the radar
d = 0.0						# m perpendicular distance to the road
l = 1.0						# m length from the projaction of the radar to the street to 
							# the spot of the antena beam
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
	global Fs
	if type(x) != ndarray:
		x = array(x)
	assert type(x) is ndarray, 'The input is not a vector'

	info = zeros((1,5)) 			# V_min, V_max, V_mean, N_veh, N_ped
	xlen = len(x)

	win = chebwin(WLEN, at = 100)		# Attenuation 100dB

	# Initialize index and threshold
	indx = 0
	threshold = 1e4					# Lineal

	# Frequencies vector
	f_t = arange(NFFT) * Fs / NFFT
	f = f_t[f_t<FLimitSpeed]

	while indx + WLEN < xlen:

		xw = x[indx:(indx+WLEN)] * win
		xw = xw - mean(xw)

		X = abs(fft.fft(xw, NFFT))[f_t<FLimitSpeed]
		XdB = 20 * log10(X)
		X_2 = X[f[X<threshold]>FLimitFlicker]
		if len(X_2) > 0:
			mn = mean(X_2)
			st = std(X_2)
			threshold = mn + 7 * st
			flat_threshold_dB = 20 * log10(threshold)

			ramp_threshold_dB = flat_threshold_dB - (f - FLimitFlicker) * G / FLimitFlicker
			threshold_dB = array([max(flat_threshold_dB, t) for t in ramp_threshold_dB])

		# Compute the power from 0 to 200 Hz to stimate the average number of pedestrians
		power_ped = sum(X[f<FLimitPedestrian])
		N_ped = Kp * power_ped

		# Compute the power from 200 Hz to 1.5 kHz to stimate the average number of vehicles
		power_veh = sum(X[f>=FLimitPedestrian])
		N_veh = Kv * power_veh

		# Creation of PDF of velocities to estimate average speed of vehicles
		temp = concatenate([zeros(sum(f<FLimitPedestrian)),X[f>=FLimitPedestrian]])
		pdf = array([max(temp[j], threshold) for j in range(len(temp))])
		pdf = pdf - threshold
		if sum(pdf) != 0:
			pdf = pdf / sum(pdf)
		f_mean = sum(f*pdf)

		v_mean = compute_speed(f_mean)

		# Finding peaks
		pks_pos = find_peaks(XdB, bandwidth = 5)
		pks_pos = pks_pos[XdB[pks_pos] > threshold_dB[pks_pos]]
		f_pks = f[pks_pos]
		v = compute_speed(f_pks[XdB[f_pks>FLimitPedestrian]>flat_threshold_dB + SNRmin])

		# Determine the v_min and v_max
		v_min, v_max = 0, 0
		if len(v) > 0:
			v_min = min(v)
			v_max = max(v)

		# update indexes
		indx = indx + WLEN - H

		# Gathering
		aux = [v_min, v_max, v_mean, N_veh, N_ped]
		info = concatenate([info, [aux]], 0)

	info = info[1:]
	v_min, v_max, me = [None] * 3
	nums = array([sum(info[:,3], 0), sum(info[:,4], 0)])
	if sum(info[:,0]!=0) != 0:
		v_min = min(info[info[:,0] != 0, 0])
		v_max = max(info[info[:,1] != 0, 1])
		me = mean(info[info[:,2] != 0, 2])
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

def downsampling(x):
	global Fs
	x_tmp = convolve(x, filter.get_filter(), 'same') * 20 * log10(8)
	p = arange(0, (len(x)/DOWNSAMPLING))
	Fs = Fs / DOWNSAMPLING
	return x_tmp[DOWNSAMPLING*p]


if __name__ == '__main__':	

	i, x = wavfile.read('testPython/sample1.wav')
	print "Read wav"
	x = array(x, dtype=float16)/2**15
	print len(x)
	x = downsampling(x)
	print len(x)
	start = time()
	data = algorithm(x)
	stop = time()
	print data
	print 'Spent: ', (stop-start), ' seconds'
