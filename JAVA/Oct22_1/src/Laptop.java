
public class Laptop implements Comparable<Laptop>{
	private int srno;
	private String make;
	private double cost;
	private int ram;
	public Laptop(int srno, String make, double cost, int ram) {
		super();
		this.srno = srno;
		this.make = make;
		this.cost = cost;
		this.ram = ram;
	}
	public int getRam() {
		return ram;
	}
	public void setRam(int ram) {
		this.ram = ram;
	}
	public int getSrno() {
		return srno;
	}
	public void setSrno(int srno) {
		this.srno = srno;
	}
	public String getMake() {
		return make;
	}
	public void setMake(String make) {
		this.make = make;
	}
	public double getCost() {
		return cost;
	}
	public void setCost(double cost) {
		this.cost = cost;
	}
	
	public Laptop() {
		super();
		this.srno = 101;
		this.make = "";
		this.cost = 1.0;
		this.ram=1;
	}
	public void disp() {
		// TODO Auto-generated method stub
		System.out.println("SrNo: "+srno+" maker: "+make+" Cost: "+cost+" RAM: "+ram);
	}	
	@Override
	public int compareTo(Laptop o) {
		// TODO Auto-generated method stub
		if(this.cost>o.cost)
		{
			return 1;
		}
		else if(this.cost<o.cost)
		{
			return -1;
		}
		else
			return 0;
	}
	
}
