//Using switch-case construct, write a menu driven program to perform basic calculations 
//(addition, subtraction, multiplication and division) on two user entered numbers.

import java.util.Scanner;

public class Ass6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter a No: ");
		int a=sc.nextInt();
		System.out.print("Enter a No: ");
		int b=sc.nextInt();
		while(Boolean.TRUE)	
		{
			System.out.println("1.addition\n2.subtraction\n3.multiplication\n4.division\n5.Exit");
			System.out.print("Enter a Choice: ");
			int ch=sc.nextInt();
			switch(ch)
			{
				case 1:
					System.out.println("Addition of "+a+"&"+b+"="+(a+b));
					break;
				case 2:
					System.out.println("Subtraction of "+a+"&"+b+"="+(a-b));
					break;
				case 3:
					System.out.println("Multipliation of "+a+"&"+b+"="+(a*b));
					break;
				case 4:
					System.out.println("Division of "+a+"&"+b+"="+(a/b));
					break;
				case 5:
					System.exit(0);
					break;
				default:
					System.out.println("Invalid Choice.");
			}
		}
	}

}
