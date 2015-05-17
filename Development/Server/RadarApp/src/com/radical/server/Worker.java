package com.radical.server;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

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

	protected void close() {
		try {
			this.socket.close();
		} catch(Exception e) {e.printStackTrace();}

	}
}