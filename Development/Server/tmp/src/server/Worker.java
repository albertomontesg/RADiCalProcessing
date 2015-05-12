package server

public class Worker extends Thread {
	protected Socket socket;
	protected Controller controller;
	protected InputStream input;
	protected OutputStream output;

	public Worker(Socket s, Controller c) {
		this.socket = s;
		this.controller = c;
		try {
			input = s.getInputStream();
			output = s.getOutputStream();
		} catch(IOException e) {
			this.close();
		}
	}

	private void close() {
		try {
			this.socket.close();
			this.controller.deleteClient();
			this.controller.deletePi();

		} catch(Exception e) {e.printStackTrace();}

	}
}