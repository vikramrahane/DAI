//Write a program to swap two variables using a third variable and without using third variable.

import java.util.Scanner;

public class Ass3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter a No for a: ");
		int a=sc.nextInt();
		System.out.print("Enter a No for b: ");
		int b=sc.nextInt();
		// using third varisble
		int temp;
		temp=a;
		a=b;
		b=temp;
		System.out.println("a="+a+" b="+b);
		
		System.out.println("without using thrd variable");
		System.out.print("Enter a No for a: ");
		 a=sc.nextInt();
		System.out.print("Enter a No for b: ");
		 b=sc.nextInt();
		 a=a+b;
		 b=a-b;
		 a=a-b;
		 System.out.println("a="+a+" b="+b);
	}

}
