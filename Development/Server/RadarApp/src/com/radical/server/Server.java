package com.radical.server;

import java.net.ServerSocket;
import java.net.Socket;

import com.radical.server.Controller;

public class Server extends Thread {
	private Controller controller;
	private ServerSocket server;

	private static final int serverPort = 30000;
	private static final int L = 64;
	
	public Server() {
		this.controller = new Controller();
		System.out.println("Server Initialized");
	}
	
	public void run() {
		try {
			server = new ServerSocket(serverPort);

			int id = 1;
			while (true) {
				// Get the socket of the input connection
				Socket socket = server.accept();
				Worker w;

				// Identification
				byte[] msg = new byte[L];
				socket.getInputStream().read(msg);
				if (msg[0] == Protocol.CONNECT_PI) {
					Pi p = new Pi(socket, this.controller, id);
					this.controller.addPi(p);
					p.sendID(id);
					p.start();
					System.out.println("Pi Connected:" + id);
					id++;
				}
				else if (msg[0] == Protocol.CONNECT_CLIENT) {
					w = new Client(socket, this.controller);
					this.controller.addClient((Client) w);
					w.start();
					System.out.println("Client Connected");
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