/*Write a program to accept the basic salary and total sales amount for a salesperson and 
 * calculate commission according to sales amount. Display the net salary and commission earned.
 *  (Net Salary = Basic Salary + Commission) The range is as follows.
*/

import java.util.Scanner;

public class Ass5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter a BAsic Salary: ");
		int b_sal=sc.nextInt();
		System.out.print("Enter a Total Sales Amount: ");
		int sale=sc.nextInt();
		double n_sal=0;
		if(sale>=5000 && sale<=7500)
		{
			n_sal=(b_sal*0.03)+b_sal;
		}
		else if(sale>=7501 && sale<=10500)
		{
			n_sal=(b_sal*0.08)+b_sal;
		}
		else if(sale>=10501 && sale<15000)
		{
			n_sal=(b_sal*0.11)+b_sal;
		}
		else if(sale>=15000)
		{
			n_sal=(b_sal*0.15)+b_sal;
		}
		else
		{
			n_sal=b_sal;
		}
		System.out.println("Net Salary of Salesman: "+n_sal);
	}

}
