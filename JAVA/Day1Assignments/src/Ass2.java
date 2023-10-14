//Write a program to add two numbers and store the result in a third variable. Print the result.
import java.util.Scanner;
public class Ass2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc=new Scanner(System.in);
		System.out.print("Enter a No: ");
		int a=sc.nextInt();
		System.out.print("Enter a No: ");
		int b=sc.nextInt();
		int c=a+b;
		System.out.println("Addition of two No is: "+c);
	}

}
