import java.util.logging.Logger;
import java.util.logging.FileHandler;
import java.util.logging.SimpleFormatter;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class IpCapture extends Thread {
	private ServerSocket server;
	private Logger logger;
	private FileHandler fh;

	private static final int serverPort = 33333;
	
	public IpCapture() {
		try {
			this.logger = Logger.getLogger("IPLog");
			this.fh = new FileHandler("/home/ubuntu/ipcapture/IPLogFile.log");  
			this.logger.addHandler(this.fh);
			SimpleFormatter formatter = new SimpleFormatter();  
        	fh.setFormatter(formatter);
			server = new ServerSocket(serverPort);

		} catch(Exception e) {e.printStackTrace();}
	}
	
	public void run() {
		FileHandler fh; 
		try {
			while (true) {
				// Get the socket of the input connection
				Socket socket = server.accept();
				byte[] msg = new byte[1024];
				if (socket.getInputStream().read(msg) != -1) {
					String ip = new String(msg);
					System.out.println(ip);
					this.logger.info(ip);
				}
				socket.close();
			}
			
		} catch(Exception e) {
			try {
				server.close();
			} catch(Exception er){ er.printStackTrace();}
			e.printStackTrace();
		}
	}
	

	public static void main(String[] args){
        new IpCapture().start();
    }
}