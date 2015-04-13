package server

import java.util.concurrent.CopyOnWriteArrayList;

public class Controller {

	private CopyOnWriteArrayList<Client> clients;
	private CopyOnWriteArrayList<Pi> pis;

	public Controller() {
		this.clients = new CopyOnWriteArrayList<Client>()
		this.pis = new CopyOnWriteArrayList<Pi>()
	}

	public void addClient(Client c) {
		clients.add(c);
	}

	public void deleteClient(Client c) {
		clients.remove(c);
	}

	public void addPi(Pi p) {
		pis.add(p);
	}

	public deletePi(Pi p) {
		pis.remove(p):
	}

	public subscribe(int id, Client c) {
		for(Pi p: pis) {
			if (p.ID == id)
				p.addSubscriber(c);
		}
	}

	public unsubscribe(int id, Client c) {
		for(Pi p: pis) {
			if (p.ID == id)
				p.deleteSubscriber(c);
		}
	}

	public receivedInfoFromPi(int id, info) {
		// save it on the database

	}

}