
public class Employee {
	private int eid;
	private String name;
	private Date1 dob;
	public Employee(int eid, String name, int d,int m, int y) {
		super();
		this.eid = eid;
		this.name = name;
		this.dob = new Date1(d,m,y);
	}
	public Employee() {
		super();
		this.eid = 1;
		this.name = "abc";
		this.dob = new Date1(1,1,2000);
	}
	void show()
	{
		System.out.println("Employee Name: "+this.name+" Employee ID: "+this.eid);
		System.out.println(" Date of Birth: ");
		this.dob.show();
	}
}
