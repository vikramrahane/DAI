import in.cdac.*;
public class Tester {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Laptop l1=new Laptop();
		Laptop l2=new Laptop(102, "apple", 72000);
		Laptop l3=new Laptop();
		System.out.println(l1);
		System.out.println(l2);
		Laptop.showcnt();
	}

}
