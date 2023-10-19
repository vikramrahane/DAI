
public class SalesPerson extends WageEmployee {
	
	private int no_item;
	private int commi;
	public SalesPerson(int eid, String name, int d, int m, int y, int hrs, int rate, int no_item, int commi) {
		super(eid, name, d, m, y, hrs, rate);
		this.no_item = no_item;
		this.commi = commi;
	}
	public SalesPerson() {
		super();
		this.no_item = 1;
		this.commi = 1;
	}
	void show()
	{
		super.show();
		System.out.println("Number of items sold: "+this.no_item+" Commission per item: "+this.commi);
		
	}
	void cal_salary()
	{
		sal=(hrs*rate)+(no_item*commi);
		System.out.println("Sales Person Salary : "+sal);
	}
}
