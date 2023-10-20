

class Circle1 implements Cloneable
{
	private int radius;

	public Circle1(int radius) {
		super();
		this.radius = radius;
	}

	public Circle1() {
		super();
		radius =1;
	}
	public double calcPeri()
	{
		return 3.142*2*radius;
	}
	public double calcArea()
	{
		return 3.142*radius*radius;
	}
	public Object clone() throws CloneNotSupportedException
	{
		return super.clone();
	}
	
}
public class Tester2 {
	public static void main(String[] args) throws CloneNotSupportedException
	{
		Circle1 c1=new Circle1(11);
		Circle1 c2=(Circle1)c1.clone();
		System.out.println(c2.calcArea());
	}
}
