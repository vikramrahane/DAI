//Write a program to find maximum of three numbers using conditional operators.

import java.util.Scanner;

public class Ass7 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter a No for a: ");
		int a=sc.nextInt();
		System.out.print("Enter a No for b: ");
		int b=sc.nextInt();
		System.out.print("Enter a No for c: ");
		int c=sc.nextInt();
		if(a>b && a>c)
		{
			System.out.println("a is maximum.");
		}
		else if(b>c)
		{
			System.out.println("b is maximum.");
		}
		else
		{
			System.out.println("c is maximum.");
		}
	}

}
