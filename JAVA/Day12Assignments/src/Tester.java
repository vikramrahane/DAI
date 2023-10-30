import java.util.*;
import java.io.*;
public class Tester {
	
	public static int readObject(File f)
	{
		int cnt=0;
		try
		{
			System.out.println("Reading Object.");
			FileInputStream fis=new FileInputStream(f);
			ObjectInputStream ois=new ObjectInputStream(fis);
			while(ois.readObject()!=null)
				cnt++;
			return cnt;
		}
		catch(Exception e)
		{
			//e.printStackTrace();
			return cnt;
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		File f=new File("account_data.dat");
		FileOutputStream fos;
		ObjectOutputStream oos;
		try
		{
			 fos=new FileOutputStream(f,true);
			 oos=new ObjectOutputStream(fos);
			 FileInputStream fis=new FileInputStream(f);
			ObjectInputStream ois=new ObjectInputStream(fis);
		
		int ch;
		do
		{
			System.out.println("1. Add record for new account holder\n"
					+ "2. Display details of all account holders.\n"
					+ "3. Deposite an amount into perticular account\n"
					+ "4. Withdraw an amount from perticular account\n"
					+ "5. Exit");
			System.out.println("Enter a choice: ");
			ch=sc.nextInt();
			switch(ch)
			{
				case 1:		
					Account a=new Account();
					System.out.println("Enter Account No: ");
					int n=sc.nextInt();
					System.out.println("Enter Customer Name: ");
					String s=sc.next();
					System.out.println("Enter Balance: ");
					double b=sc.nextDouble();
					a.setBalance(b);
					a.setName(s);
					a.setNo(n);
					
					oos.writeObject(a);
					oos.reset();
					System.out.println("object is saved");
					
					break;
				case 2:
					List<Account> l=new ArrayList<Account>();
					
					try
					{
						Object obj;
						System.out.println("Reading Object.");
						while(((obj=ois.readObject()) instanceof Account))
						{
							l.add((Account) obj);
							System.out.println("a");
						}
						l.forEach((x) -> System.out.println(x+"  "));
						ois.close();
					}
					catch(Exception e)
					{
						e.printStackTrace();
						System.out.println("End");
					}
					break;
				case 3:
					
					break;
				case 4:
					
					break;
				case 5:
					System.exit(0);
					break;
				default:
					System.out.println("Wrong Choice!");
			}
		}while(ch!=5);
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}

	}

}
