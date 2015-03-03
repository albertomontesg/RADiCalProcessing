import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt


CHUNK = 1024
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 22000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []
d = np.array([])
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    d=np.append(d,np.fromstring(data,np.float32))
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

plt.figure(1)
plt.plot(d)
plt.show()
plt.figure(2)
plt.specgram(d,Fs=RATE)
plt.show()
