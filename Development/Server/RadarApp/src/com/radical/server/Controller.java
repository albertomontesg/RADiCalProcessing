package com.radical.server;

import java.util.concurrent.CopyOnWriteArrayList;

public class Controller {

	private CopyOnWriteArrayList<Client> clients;
	private CopyOnWriteArrayList<Pi> pis;
	private Storage storage;

	public Controller() {
		this.clients = new CopyOnWriteArrayList<Client>();
		this.pis = new CopyOnWriteArrayList<Pi>();
		this.storage = new Storage();
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

	public void deletePi(Pi p) {
		pis.remove(p);
	}

	public boolean subscribe(int id, Client c) {
		for(Pi p: pis) {
			if (p.getID() == id) {
				p.addSubscriber(c);
				return true;
			}
		}
		return false;
	}

	public void unsubscribe(Client c) {
		for(Pi p: pis)
			p.deleteSubscriber(c);
	}

	public void saveCapture(byte[] mess) {
		this.storage.addValue(mess);
	}
	
	public void sendHistoric(Client c) {
		char[] str = (this.storage.getHistoric(c.idSubscribed)).toCharArray();
		byte[] mess = new byte[64];
		mess[0] = Protocol.DATA;
		for (int i = 1; i < mess.length && i <= str.length; i++) mess[i] = (byte) str[i-1];
		c.send(mess);
	}

	public byte[] getLast(int id) {
		for (Pi p : pis) {
			if (p.getID() == id)
				System.out.println("Send last: " + new String(p.getLast()));
				return p.getLast();
		}
		char[] str = ("0\t0.0\t0.0\t0.0\t0\t0\t0").toCharArray();
		byte[] mess = new byte[64];
		mess[0] = Protocol.DATA;
		for (int i = 1; i < mess.length && i <= str.length; i++) mess[i] = (byte) str[i-1];
		return mess;
	}
}