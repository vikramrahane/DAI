package in.cdac;

public class Laptop {
	private int srno;
	private String make;
	private double cost;
	private static int cnt;

	public Laptop(int srno, String make, double cost) {
		
		this.srno = srno;
		this.make = make;
		this.cost = cost;
		cnt++;
	}

	public Laptop() {
		this.srno = 101;
		this.make = "hp";
		this.cost = 60000;
		cnt++;
	}

	@Override
	public String toString() {
		return "Laptop [srno=" + srno + ", make=" + make + ", cost=" + cost + "]";
	}
	public static void showcnt()
	{
		System.out.println("Number of objects= "+cnt);
	}
	

}
