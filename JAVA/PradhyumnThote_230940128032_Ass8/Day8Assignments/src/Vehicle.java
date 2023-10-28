import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Vehicle implements Comparable<Vehicle>{
	private int vno;
	private String name;
	private double cost;
	public int getVno() {
		return vno;
	}
	public void setVno(int vno) {
		this.vno = vno;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public double getCost() {
		return cost;
	}
	public void setCost(double cost) {
		this.cost = cost;
	}
	public Vehicle(int vno, String name, double cost) {
		super();
		this.vno = vno;
		this.name = name;
		this.cost = cost;
	}
	public Vehicle() {
		super();
		this.vno = 0;
		this.name = " ";
		this.cost = 0.0;
	}
	public void printVehicle()
	{
		System.out.println("Vehicle No: "+vno+" Name:"+name+" Cost: "+cost);
	}
	public void acceptVehicle()
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter Vehicle No: ");
		this.setVno(sc.nextInt());
		System.out.println("Enter Name of Vehicle: ");
		this.setName(sc.next());
		System.out.println("Enter Cost of Vehicle: ");
		this.setCost(sc.nextDouble());
	}
	@Override
	public int compareTo(Vehicle o) {
		// TODO Auto-generated method stub
		if(this.cost>o.getCost())
			return 1;
		else if(this.cost<o.getCost())
			return -1;
		else 
			return 0;
	}
}
