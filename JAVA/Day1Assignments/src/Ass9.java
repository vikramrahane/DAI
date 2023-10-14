//Write a program to display whether a user entered number is prime or not.

import java.util.Scanner;

public class Ass9 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter a No: ");
		int n=sc.nextInt();
		
		for(int i=2;i<n;i++)
		{
			if(i==n-1)
			{
				System.out.println(n+" is Prime No.");
				break;
			}
			if(n%i==0)
			{
				System.out.println(n+" is not Prime No.");
				break;
			}
			
		}
	}

}
