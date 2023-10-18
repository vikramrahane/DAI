import java.util.Scanner;
public class Accountholder {
	private int accno;
	private String name;
	private double balance;
	
	
	public Accountholder() {
	}
	
	public Accountholder(int accno, String name, double balance) {
		this.accno = accno;
		this.name = name;
		this.balance = balance;
	}
	
	public void deposit(int amount)
	{
		balance=balance + amount;
	}
	
	public void withdraw(int amount)
	{
		balance= balance - amount;
	}

	@Override
	public String toString() {
		return "Accountholder [accno=" + accno + ", name=" + name + ", balance=" + balance + "]";
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

	public int getAccno() {
		return accno;
	}
	
	

}
