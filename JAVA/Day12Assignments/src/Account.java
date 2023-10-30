import java.io.Serializable;

public class Account implements Serializable{
	private int no;
	private String name;
	private double balance;
	
	public Account(int no, String name, double balance) {
		super();
		this.no = no;
		this.name = name;
		this.balance = balance;
	}
	public Account() {
		super();
	}
	public int getNo() {
		return no;
	}
	public void setNo(int no) {
		this.no = no;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public double getBalance() {
		return balance;
	}
	public void setBalance(double balance) {
		this.balance = balance;
	}
	void deposit(double x)
	{
		if(x>0)
		{
			double total=x+this.getBalance();
			this.setBalance(total);
			System.out.println("your account is credited with "+x);
			System.out.println("your total Balance is "+this.getBalance());
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
			double total=this.getBalance()-x;
			if(total>=0)
			{
				this.setBalance(total);
				System.out.println("your account is debited with "+x);
				System.out.println("your total Balance is "+this.getBalance());
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
		return "Name: "+this.name+" Acc No: "+this.no+" Balance: "+this.balance;
		
	}
}
