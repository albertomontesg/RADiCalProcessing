package server

import Protocol;

public class Pi extends Worker {
	public int ID;
	private CopyOnWriteArrayList<Client> subscribers;

	public Pi(Socket s, Controller c, int id) {
		super(s, c);
		this.ID = id;
		System.out.println("Pi Worker Started");
	}

	public void run() {
		try {
			byte[] mess = new byte[64];
			while((input.read(mess)) != -1) {
				if (mess[0] == Protocol.DISCONNECT_PI) {
					this.deleteAllSubscribers();
					this.controller.deletePi(this);
				} else if (mess[0] == Protocol.DATA) {
					this.manageData(mess);
				}
			}
		} catch(Exception e) {
			this.close()
		}
	}

	public void addSubscriber(Client c) {
		this.subscribers.add(c);
	}

	public void deleteSubscriber(Client c) {
		this.subscribers.delete(c);
	}

	public void deleteAllSubscribers() {
		this.subscribers.clear();
	}

	public CopyOnWriteArrayList<Pi> getSubscribers() {
		return this.subscribers;
	}

	private void manageData(byte[] mess) {
		/*
		Save on the database the data received from the Raspberry Pi with ID #
		*/

		for (Client c: subscribers) {
			c.send(mess);
		}
	}
}