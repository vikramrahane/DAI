
public class WageEmployee extends Employee {
	protected int hrs;
	protected int rate;
	protected int sal;
	public WageEmployee(int eid, String name, int d, int m, int y, int hrs, int rate) {
		super(eid, name, d, m, y);
		this.hrs = hrs;
		this.rate = rate;
	}
	public WageEmployee() {
		super();
		this.hrs = 1;
		this.rate = 100;
	}
	void show()
	{
		super.show();
		System.out.println("Working Hours: "+this.hrs+" Rate/Hr: "+this.rate);
		
	}
	void cal_salary()
	{
		sal=hrs*rate;
		System.out.println("Salary : "+this.sal);
	}
	
}
