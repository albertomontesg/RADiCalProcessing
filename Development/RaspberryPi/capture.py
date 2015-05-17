import pyaudio

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1L
RATE = 44100
DEVICE_ID = 0

class Capture(object):
	"""docstring for Capture"""
	def __init__(self, logger):
		super(Capture, self).__init__()
		self.audio = pyaudio.PyAudio()
		self.logger = logger


	def record(self, time = 30):
		self.stream = p.open(format=FORMAT,
							channels=CHANNELS,
							rate=RATE,
							input=True,
							input_device_index=DEVICE_ID,
							frames_per_buffer=CHUNK)
		logger.info("Start Recording")

		frames = []
		for i in range(0, int(RATE * time / CHUNK)):
			data = stream.read(CHUNK)
			frames.append(data)

		logger.info("Stop Recording")

		stream.start_stream()
		stream.close()
		
		return frames