
from threading import Thread


class Process(Thread):

	def __init__(self, condition):
		Thread.__init__(self)
		self.is_processing = False
		self.data_to_process = None
		self.cv = condition

	def run(self):
		while True:
			self.cv.acquire()
			while not self.is_processing:
				self.cv.wait()
			proces = self.data_to_process
			self.cv.release()



	def send_data_to_process(self, data):
		self.cv.acquire()
		
		
		while not self.is_processing:
			self.cv.wait()
		self.data_to_process = data
		self.cv.release()