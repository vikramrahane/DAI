public class AccountHolder {
	
	public static int cnt;
	int accno;
	String name;
	double bal;
	
	// Constructors
	public AccountHolder()
	{
		accno=1;
		name="xyz";
		bal=1000.00;
	}
	public AccountHolder(int accno,String name,double bal)
	{
		this.accno=accno;
		this.name=name;
		this.bal=bal;
	}
	// Setter Methods
	void set_accno(int x)
	{
		this.accno=x;
	}
	void set_name(String x)
	{
		this.name=x;
	}
	void set_bal(double x)
	{
		this.bal=x;
	}
	// Getter Methods
	int get_accno()
	{
		return this.accno;
	}
	String get_name()
	{
		return this.name;
	}
	double get_bal()
	{
		return this.bal;
	}
	// class methods
	void deposit(double x)
	{
		if(x>0)
		{
			double total=x+this.get_bal();
			this.set_bal(total);
			System.out.println("your account is credited with "+x);
			System.out.println("your total Balance is "+this.get_bal());
		}
		else
		{
			System.out.println("Please enter valid amount");
		}
	}
	void withdraw(double x)
	{
		if(x>0)
		{
			double total=this.get_bal()-x;
			if(total>=0)
			{
				this.set_bal(total);
				System.out.println("your account is debited with "+x);
				System.out.println("your total Balance is "+this.get_bal());
			}
			else
			{
				System.out.println("you don't have sufficient balance in your account.");
			}
		}
		else
		{
			System.out.println("Please enter valid amount");
		}
	}
	public String toString()
	{
		return "Name: "+this.name+" Acc No: "+this.accno+" Balance: "+this.bal;
		
	}
}
