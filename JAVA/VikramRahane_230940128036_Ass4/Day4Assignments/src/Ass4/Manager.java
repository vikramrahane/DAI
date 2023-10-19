package Ass4;

public class Manager extends Employee {
	private double petro_allo,food_allo,other_allo, g_sal,n_sal;

	public Manager(int eid, String name, double b_sal) {
		super(eid, name, b_sal);
		petro_allo=0.08*b_sal;
		food_allo=0.12*b_sal;
		other_allo=0.04*b_sal;
		g_sal=b_sal+food_allo+other_allo+petro_allo;
		n_sal=g_sal-pf;
	}
	
	public Manager() {
		super();
		petro_allo=0.08*0;
		food_allo=0.12*0;
		other_allo=0.04*0;
		g_sal=b_sal+food_allo+other_allo+petro_allo;
		n_sal=g_sal-pf;
	}

	void show()
	{
		System.out.println("Manager Details");
		super.show();
		System.out.println("Petrol Allowance: "+this.petro_allo+" Food Allowance: "+this.food_allo);
		System.out.println("Other Allowances: "+this.other_allo);
		System.out.println("Gross Salary: "+this.g_sal);
		System.out.println("Net Salary: "+this.n_sal);
		
	}
}
