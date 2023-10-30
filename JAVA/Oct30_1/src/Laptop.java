import java.io.Serializable;

public class Laptop implements Serializable {
	private int id;
	private String make;
	private double cost;
	public Laptop() {
		super();
	}
	public Laptop(int id, String make, double cost) {
		super();
		this.id = id;
		this.make = make;
		this.cost = cost;
	}
	@Override
	public String toString() {
		return "Laptop [id=" + id + ", make=" + make + ", cost=" + cost + "]";
	}
	
}
