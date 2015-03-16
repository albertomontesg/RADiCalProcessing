import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.CopyOnWriteArrayList;

public class Server extends Thread {
	private CopyOnWriteArrayList<ClientWorker> clients;
	private CopyOnWriteArrayList<PiWorker> pi;
	private ServerSocket server;

	private static final int serverPort = 30000;
	
	public Server() {
		clients = new CopyOnWriteArrayList<ClientWorker>();
		pi = new CopyOnWriteArrayList<PiWorker>();
	}
	
	public void run() {
		try {
			server = new ServerSocket(serverPort);
			while (true) {
				// Get the socket of the input connection
				Socket socket = server.accept();
				// byte[] auth = new byte[1024];
				// socket.getInputStream().read(auth);
				// System.out.println((int)auth[0]);
				// if (auth[0] == 1) {
				ClientWorker w = new ClientWorker(socket);
				clients.add(w);
				w.start();
				// }
				// else if (auth[0] == 2) {
				// 	PiWorker p = new PiWorker(socket);
				// 	pi.add(p);
				// 	p.start();
				// }

			}
			
		} catch(Exception e) {
			try {
				server.close();
			} catch(Exception er){ er.printStackTrace();}
			e.printStackTrace();
		}
	}
	
	class PiWorker extends Thread {
		private Socket socket;
		protected InputStream input;
		protected OutputStream output;
		
		public PiWorker(Socket s) {
			this.socket = s;
			try {
				input = socket.getInputStream();
				output = socket.getOutputStream();
				System.out.println("New Pi started " + this.getName());

			} catch (IOException e) {
				e.printStackTrace();
				pi.remove(this);
			}
		}

		public void run() {
			try {
				
				String line;
				
				// While there isn't an EOF keep reading from the client and sending the echo answer
				byte[] cbuf = new byte[1024];
				int counter = 1;
				while((input.read(cbuf)) != -1) {
					String str = new String(cbuf);
					System.out.println(this.getName() + ": " + str);
					for(ClientWorker w : clients) {
						if (counter % 10 == 0 && !w.socket.isConnected()) {
							w.socket.close();
							clients.remove(w);
						}
						w.output.write(cbuf);
						w.output.flush();
						System.out.println("Send to " + w.getName() + ": " + str);
					}
					counter++;
				}
				System.out.println("Worker ended");
				// Send an End of Stream so the client would receive and EOF
				socket.shutdownInput();
				
				// Close all the streams and connections
				input.close();
				output.close();
				socket.close();
			} catch (Exception e) {
				clients.remove(this);
				e.printStackTrace();
			}
		}

	}

	class ClientWorker extends Thread {
		private Socket socket;
		protected InputStream input;
		protected OutputStream output;
		
		public ClientWorker(Socket s) {
			this.socket = s;
			try {
				input = socket.getInputStream();
				output = socket.getOutputStream();
				System.out.println("New Worker started " + this.getName());

			} catch (IOException e) {
				e.printStackTrace();
				clients.remove(this);
			}
		}

		public void run() {
			try {
				
				String line;
				
				// While there isn't an EOF keep reading from the client and sending the echo answer
				byte[] cbuf = new byte[1024];
				int counter = 1;
				while((input.read(cbuf)) != -1) {
					String str = new String(cbuf);
					System.out.println(this.getName() + ": " + str);
					for(ClientWorker w : clients) {
						if (w != this) {
							if (counter % 10 == 0 && !w.socket.isConnected()) {
								w.socket.close();
								clients.remove(w);
							}
							try {
								w.output.write(cbuf);
							} catch (Exception er) {
								clients.remove(w);
							}
							
							w.output.flush();
							System.out.println("Send to " + w.getName() + ": " + str);
						}
						
					}
					counter++;
				}
				System.out.println("Worker ended");
				// Send an End of Stream so the client would receive and EOF
				socket.shutdownInput();
				
				// Close all the streams and connections
				input.close();
				output.close();
				socket.close();
			} catch (Exception e) {
				clients.remove(this);
				e.printStackTrace();
			}
		}
	}

	public static void main(String[] args){
        new Server().start();
    }	
}