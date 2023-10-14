/*
 * Write a program to print whether user entered number is an Armstrong number.  
 * Armstrong number is one for which the sum of the cube of all its digits is same as the number.
 *  For example, 153 = (1*1*1) + (5*5*5) + (3*3*3)
 */

import java.util.Scanner;

public class Ass8 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter a No for a: ");
		int a=sc.nextInt();
		int temp=a,sum=0,d,cube;
		for(int i=1;i<100000;i++) // Use 'for' Armstrong No in 1 to 100000 range
		{
			temp=i;
			sum=0;
			while(temp>0)
			{
				d=temp%10;
				cube=d*d*d;
				sum=sum+cube;
				temp=temp/10;
			}
			if(sum==i)
			{
				System.out.println(i+" is armstrong No.");
			}
			else
			{
				//System.out.println(i+" is not a armstrong No.");
			}
		}
	}

}
