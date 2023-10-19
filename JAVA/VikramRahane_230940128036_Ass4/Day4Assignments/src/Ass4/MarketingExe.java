package Ass4;

public class MarketingExe extends Employee {
	private double km;
	private final static int tele=1000;
	private double tour_allo,g_sal,n_sal;
	public MarketingExe(int eid, String name, double b_sal, double km) {
		super(eid, name, b_sal);
		this.km = km;
		this.tour_allo = 5*km;
		g_sal=b_sal+tour_allo+tele;
		n_sal=g_sal-pf;
	}
	public MarketingExe() {
		super();
		this.km = 1;
		this.tour_allo = 5*1;
	}
	void show()
	{
		System.out.println("Marketing Executive Details");
		super.show();
		System.out.println("Kilometers travelled: "+this.km+" Telephone Allowance: "+tele);
		System.out.println("Tour Allowance: "+this.tour_allo);
		System.out.println("Gross Salary: "+this.g_sal);
		System.out.println("Net Salary: "+this.n_sal);
		
	}
	
}
