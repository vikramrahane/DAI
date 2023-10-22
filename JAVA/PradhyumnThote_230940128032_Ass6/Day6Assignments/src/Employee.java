import java.util.Scanner;

public class Employee {
	
		private int id;
		private String name;
		private double sal;
		public Employee(int id, String name, double sal) {
			super();
			this.id = id;
			this.name = name;
			this.sal = sal;
		}
		public Employee() {
			super();
			this.id = 101;
			this.name = "Vicky";
			this.sal = 100000;
		}
		public int getId() {
			return id;
		}
		public void setId(int id) {
			this.id = id;
		}
		public String getName() {
			return name;
		}
		public void setName(String name) {
			this.name = name;
		}
		public double getSal() {
			return sal;
		}
		public void setSal(double sal) {
			this.sal = sal;
		}
		public void disp()
		{
			System.out.println("Employee Id: "+id+" Name: "+name+" Salary: "+sal);
		}
		public void accept_emp()
		{
			Scanner sc=new Scanner(System.in);
			System.out.println("Enter Employee Id: ");
			setId(sc.nextInt());
			System.out.println("Enter Name: ");
			setName(sc.next());
			System.out.println("Enter Salary: ");					
			setSal(sc.nextDouble());
		}
}
