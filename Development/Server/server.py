import threading
import socket

#HOST = "127.0.0.1"
HOST = "52.10.85.244"
PORT = 40005


class Server(threading.Thread):

	def __init__(self):
		super(Server, self).__init__()
		self.clients = []
		self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serverSocket.bind((HOST, PORT))

	def run(self):
		while True:
			try:
				self.serverSocket.listen(5)
				conn, addr = serverSocket.accept()
				print 'Connected by', addr
				w = Server.Worker(conn)
				self.clients.append(w)
				print clients
				w.start()
			except:
				self.serverSocket.close()

	class Worker(threading.Thread):

		def __init__(self, socket):
			self.socket = socket
			print "Worker started:", len(clients)

		def run(self):
			con = self.socket
			while True:
				try:
					data = con.recv(1024)
					print 'Received:', data 
					for c in clients:
						c.socket.sendall(data)
				except:
					con.close()

if __name__ == "__main__":
	s = Server()
	s.start()