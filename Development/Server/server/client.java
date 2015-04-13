package server

import server.Worker;

public class Client extends Worker {
	private int idSubscribed;

	public Client(Socket s, Controller c) {
		super(s, c);
		this.idSubscribed = 0;
	}

	public void run() {
		try {
			byte[] mess = new byte[64];
			while((input.read(mess)) != -1) {
				if (mess[0] == Protocol.SUBSCRIBE) {
					//mess[1:2] define the id of the Pi
					id
					this.idSubscribed = id;
					this.controller.subscribe(id, this)
				} else if (mess[0] == Protocol.UNSUBSCRIBE) {
					//mess[1:2] define the id of the Pi
					id
					this.idSubscribed = 0;
					this.controller.unsubscribe(id, this)
				} else if (mess[0] == Protocol.DISCONNECT_CLIENT) {
					this.controller.unsubscribe(this.idSubscribed, this)
					this.controller.deleteClient(this);
				}
			}
		} catch(Exception e) {
			this.close()
		}
	}
}