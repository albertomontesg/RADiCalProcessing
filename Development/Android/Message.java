

public class Message {
	private int id, num, ped, time;
	private float min, max, mean;
	
	public Message(String str) {
		String[] parts = str.split("\t");
		this.id = Integer.parseInt(parts[0]);
		this.min = Float.parseFloat(parts[1]);
		this.max = Float.parseFloat(parts[2]);
		this.mean = Float.parseFloat(parts[3]);
		this.num = Integer.parseInt(parts[4]);
		this.ped = Integer.parseInt(parts[5]);
		this.time = Integer.parseInt(parseInt[6]);
	}

	public int getId(){
		return this.id;
	}

	public float getMin() {
		return this.min;
	}

	public float getMax() {
		return this.max;
	}

	public float getMean() {
		return this.mean;
	}

	public int getNum(){
		return this.num;
	}

	public int getPed(){
		return this.ped;
	}

	public int getTime(){
		return this.time;
	}

}