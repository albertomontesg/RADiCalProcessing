package server

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
	private Controller controller
	private ServerSocket server;

	private static final int serverPort = 30000;
	private static final int L = 64;
	
	public Server() {
		this.controller = new Controller();
	}
	
	public void run() {
		try {
			server = new ServerSocket(serverPort);

			int id = 1000;
			while (true) {
				// Get the socket of the input connection
				Socket socket = server.accept();
				Worker w;

				// Identification
				byte[] id = new byte[L];
				socket.getInputStream().read(id);
				if (id[0] == Protocol.CONNECT_PI) {
					w = new Pi(socket, this.controller, id);
					this.controller.addClient(w);
					w.start();
					id++;
				}
				else if (id[0] == Protocol.CONNECT_CLIENT) {
					w = new Client(socket, this.controller);
					this.controller.addPi(w);
					w.start();
				}

			}
			
		} catch(Exception e) {
			try {
				server.close();
			} catch(Exception er){ er.printStackTrace();}
			e.printStackTrace();
		}
	}

	public static void main(String[] args){
        new Server().start();
    }	
}