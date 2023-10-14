//Write a program to check if user entered number is perfect number. (A perfect number is 
//a number for which sum of its factors equals that number e.g. 6=1+2+3,  28=1+2+4+7+14)
import java.util.Scanner;

public class Ass12 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		try
		{			
			System.out.print("Enter a No: ");
			int n=sc.nextInt();
			int temp=n,sum=0;
			for(int i=1;i<n;i++)
			{
				if(temp%i==0)
				{
					sum=sum+i;				
				}				
			}
			if(sum==n)
			{
				System.out.println(n+" is a perfect No.");
			}
			else
			{
				System.out.println(n+" is not a perfect No.");
			}
		}
		finally
		{
			sc.close();
		}
	}
}
