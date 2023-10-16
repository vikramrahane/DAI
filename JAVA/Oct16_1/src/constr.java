class laptop {
	private int srno;
	private String make;
	private double cost;
	
	public laptop()
	{
		srno=101;
		make="hp";
		cost=30000;
		//System.out.println("no argument constructor..);
	}
	
	public laptop(int sno, String m, double c)
	{
		srno=sno;
		make=m;
		cost=c;
		//System.out.println("parameterized constructor..");
	}
	
	public String toString()
	{
		return srno+" "+make+" "+cost;
	}
}
public class constr
{
	public static void main(String[] args) {
		laptop l1= new laptop();
		laptop l2= new laptop(102,"dell",43000);
		laptop l3= new laptop();
		System.out.println(l1);
		System.out.println(l2);
		System.out.println(l3);
	}

}
