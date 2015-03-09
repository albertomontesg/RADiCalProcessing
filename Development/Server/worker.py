

class Worker(Thread):

	def __init__(self, request):
		self.socket = request

	def run(self):
		con = self.socket
		while True:
			con.recv(1024)
