package in.cdac;

public class Employee {
	private int empid;
	private String name;
	private Date dob;
	
	public Employee() {
		empid=101;
		name="ab";
		dob=new Date();
	}

	public Employee(int empid, String name, int d, int m, int y) {
		this.empid = empid;
		this.name = name;
		this.dob = new Date(d,m,y);
	}
	
	public void show() {
		System.out.println(empid);
		System.out.println(name);
		dob.show();
	}
	
	
	
}
