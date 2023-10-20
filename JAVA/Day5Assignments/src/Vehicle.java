
public class Vehicle implements Cloneable {
	private int vehno;
	private String vehname;
	private double price;
	public int getVehno() {
		return vehno;
	}
	public void setVehno(int vehno) {
		this.vehno = vehno;
	}
	public String getVehname() {
		return vehname;
	}
	public void setVehname(String vehname) {
		this.vehname = vehname;
	}
	public double getPrice() {
		return price;
	}
	public void setPrice(double price) {
		this.price = price;
	}
	public Vehicle(int vehno, String vehname, double price) {
		super();
		this.vehno = vehno;
		this.vehname = vehname;
		this.price = price;
	}
	public Vehicle() {
		super();
		this.vehno = 123;
		this.vehname = "dfg";
		this.price = 0.0;
	}
	public Object clone() throws CloneNotSupportedException
	{
		return super.clone();
	}
	public void disp()
	{
		System.out.println("Vehicle No: "+vehno);
		System.out.println("Vehicle Name: "+vehname);
		System.out.println("Vehicle Price: "+price);
	}
}
