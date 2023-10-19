import java.util.Scanner;
public class Ass1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int i;
		Scanner sc=new Scanner(System.in);
		AccountHolder[] cust=new AccountHolder[5];
		for(i=0;i<cust.length;i++)
		{
			cust[i]=new AccountHolder();
		}
		AccountHolder.cnt=0;
		int ch;
		do
		{
			System.out.println("1. Add record for account holder\n"
					+ "2. Display details of all account holders.\n"
					+ "3. Deposite an amount into perticular account\n"
					+ "4. Withdraw an amount from perticular account\n"
					+ "5. Exit");
			System.out.println("Enter a choice: ");
			ch=sc.nextInt();
			switch(ch)
			{
				case 1:					
					System.out.println("Enter Account No, Customer Name and Balance: ");
					int n=sc.nextInt();
					String s=sc.next();
					double b=sc.nextDouble();
					if(AccountHolder.cnt>=5)
					{
						System.out.println("You can add only 5 Account Holders.");
					}
					else
					{
						cust[AccountHolder.cnt].set_accno(n);
						cust[AccountHolder.cnt].set_bal(b);
						cust[AccountHolder.cnt].set_name(s);
						AccountHolder.cnt++;
					}
					break;
				case 2:
					for(i=0;i<AccountHolder.cnt;i++)
					{
						System.out.println((i+1)+" Account Holder Details: ");
						System.out.println(cust[i]);//toString method call
						//System.out.println("Account No: "+cust[i].get_accno());
						//System.out.println("Name: "+cust[i].get_name());
						//System.out.println("Balance: "+cust[i].get_bal());
						System.out.println();
					}
					break;
				case 3:
					System.out.println("Enter a account No to Deposit: ");
					int a_no=sc.nextInt();
					for(i=0;i<cust.length;i++)
					{
						if(cust[i].get_accno()==a_no)
						{
							System.out.println("Enter amount to Deposit in Account No "+a_no);
							int amt=sc.nextInt();
							cust[i].deposit(amt);
							break;
						}
						else
						{
							if(i==4)
								System.out.println("Given Account No does not Exists.");
						}

					}
					break;
				case 4:
					System.out.println("Enter a account No to Withdrawl: ");
					a_no=sc.nextInt();
					for(i=0;i<cust.length;i++)
					{
						if(cust[i].get_accno()==a_no)
						{
							System.out.println("Enter amount to Withdrawl in Account No "+a_no);
							int amt=sc.nextInt();
							cust[i].withdraw(amt);
							break;
						}
						else
						{
							if(i==4)
								System.out.println("Given Account No does not Exists.");
						}

					}
					break;
				case 5:
					System.exit(0);
					break;
				default:
					System.out.println("Wrong Choice!");
			}
		}while(ch!=5);
	}

}