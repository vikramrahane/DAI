package in.cdac;

public class Wageemployee extends Employee {
	private int hours;
	private int rate;
	
	
	public Wageemployee() {
		super();
		hours=0;
		rate=0;
	}


	public Wageemployee(int hours, int rate,int id, String n,int d,int m, int y) {
		super(id,n,d,m,y);
		this.hours = hours;
		this.rate = rate;
	}
	
	public void show() {
		super.show();
		System.out.println(hours);
		System.out.println(rate);
	}
	

}
