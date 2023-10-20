interface Polygon
{
	public double calcArea();
	public double calcPeri();
}

class Circle implements Polygon
{
	private int radius;

	public Circle() {
		radius=1;
	}
	public Circle(int r)
	{
		radius=r;
	}
	public double calcArea()
	{
		return 3.142*radius*radius;
	}
	public double calcPeri()
	{
		return 2*3.142*radius;
	}
}

class Rectangle implements Polygon
{
	private int len, brd;
	
	public Rectangle() {
		len=brd=1;
	}
	public Rectangle (int l, int b) {
		len=l;
		brd=b;
	}
	public double calcArea() {
		return len*brd;
	}
	public double calcPeri() {
		return 2*(len+brd);
	}
}

class Square extends Rectangle
{
	private int len, brd;
	
	public Square() {
		super();
	}
	public Square (int s) {
		super(s,s);
	}
	public double calcArea() {
		return super.calcArea();
	}
	public double calcPeri() {
		return super.calcPeri();
	}
}
public class Tester1 {

	public static void main(String[] args) {
		Polygon p= new Square(10);
		System.out.println(p.calcArea());
		System.out.println(p.calcPeri());

	}

}
