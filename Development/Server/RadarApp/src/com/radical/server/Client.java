package com.radical.server;

import java.io.IOException;
import java.net.Socket;

import com.radical.server.Worker;

public class Client extends Worker {
	protected int idSubscribed;

	public Client(Socket s, Controller c) {
		super(s, c);
		this.idSubscribed = -1;
	}

	public void run() {
		try {
			byte[] mess = new byte[64];
			while((input.read(mess)) != -1) {
				if (mess[0] == Protocol.SUBSCRIBE) {
					//mess[1:2] define the id of the Pi
					// TODO
					int id = (int) mess[1];
					
					this.idSubscribed = id;
					boolean subscribed = this.controller.subscribe(id, this);
					if(subscribed) {
						System.out.println("Client subscribed to radar: "+ id);
						this.controller.sendHistoric(this);
					}
				} else if (mess[0] == Protocol.UNSUBSCRIBE) {
					//mess[1:2] define the id of the Pi
					// TODO
					this.idSubscribed = -1;
					this.controller.unsubscribe(this);
					System.out.println("Client unsubscribed to radar");
				} else if (mess[0] == Protocol.DISCONNECT_CLIENT) {
					this.controller.unsubscribe(this);
					this.controller.deleteClient(this);
					
					this.close();
				}
				
				// Flush all the data from the buffer
				for(int j = 0; j < mess.length; j++) mess[j] = 0;
			}
			this.close();
		} catch(Exception e) {
			this.close();
		}
	}
	
	public void close() {
		try {
			this.socket.close();
			System.out.println("Client closed");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public void send(byte[] mess) {
		try {
			output.write(mess);
		} catch (Exception e) {e.printStackTrace();}
	}
}