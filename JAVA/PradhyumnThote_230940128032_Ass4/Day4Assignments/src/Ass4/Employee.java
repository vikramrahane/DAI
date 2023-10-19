package Ass4;

public class Employee {
	private int eid;
	private String name;
	protected double b_sal;
	protected double pf;
	public Employee(int eid, String name, double b_sal) {
		super();
		this.eid = eid;
		this.name = name;
		this.b_sal = b_sal;
		this.pf = b_sal*0.125;
	}
	public Employee() {
		super();
		this.eid =1;
		this.name ="abc";
		this.b_sal =1.0;
		this.pf=1;
	}
	void show()
	{
		System.out.println("Employee Name: "+this.name+" Employee ID: "+this.eid);
		System.out.println("Employee Basic Salary: "+this.b_sal);
		System.out.println("Employee PF: "+this.pf);
		
	}
	
}
