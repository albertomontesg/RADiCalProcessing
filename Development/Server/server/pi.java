package server

public class Pi extends Worker {
	public int ID;
	private CopyOnWriteArrayList<Pi> subscribers;

	public Pi(Socket s, Controller c, int id) {
		super(s, c);
		this.ID = id;
		System.out.println("Pi Worker Started");
	}

	public void run() {
		try {
			byte[] mess = new byte[64];
			while((input.read(mess)) != -1) {
				
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

	public CopyOnWriteArrayList<Pi> getSubscribers() {
		return this.subscribers;
	}
}