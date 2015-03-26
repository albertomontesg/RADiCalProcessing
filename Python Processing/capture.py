import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

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

print("* recording")

frames = []
d = np.array([])
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

capture = np.array(frames)
