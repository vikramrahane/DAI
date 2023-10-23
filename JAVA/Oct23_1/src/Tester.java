import java.util.*;
class Product implements Comparable<Product>{
	private int pid;
	private String name;
	private double cost;
	
	public Product(int pid, String name, double cost) {
		super();
		this.pid = pid;
		this.name = name;
		this.cost = cost;
	}
	public void display()
	{
		System.out.println("pid : "+pid+" name : "+name+" cost : "+cost);
	}
	
	
	@Override
	public int hashCode() {
		return Objects.hash(cost, name, pid);
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Product other = (Product) obj;
		return Double.doubleToLongBits(cost) == Double.doubleToLongBits(other.cost) && Objects.equals(name, other.name)
				&& pid == other.pid;
	}
	@Override
	public int compareTo(Product o) {
		if(this.cost > o.cost)
			return 1;
		else if(this.cost < o.cost)
			return -1;
		else
			return 0;
	}
}

public class Tester {

	public static void main(String[] args) {
		Set<Product> s=new HashSet<>();
		s.add(new Product(51,"marker",60));
		s.add(new Product(52,"projector",40000));
		s.add(new Product(53,"keyboard",500));
		s.add(new Product(53,"keyboard",500));
		for(Product p:s)
			{
				System.out.println(p.hashCode());
				p.display();
				System.out.println();
			}
		
		Set<Product> ts=new TreeSet<>();
		ts.add(new Product(51,"marker",60));
		ts.add(new Product(52,"projector",40000));
		ts.add(new Product(53,"keyboard",500));
		ts.add(new Product(53,"keyboard",5000));
		ts.add(new Product(54,"keyboard",5000));
		for(Product p:ts)
			{
				p.display();
			}
	}

}
