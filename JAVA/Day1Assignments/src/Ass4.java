/*
 Write a program to calculate Net Salary of an employee. Accept Basic Salary (BS) from the user.
 	HRA is 15% of BS
 	DA is 30% of BS											
 	PF is 12.5% of GS										
 	Gross Salary is BS + HRA + DA									
 	Net Salary = Gross Salary – PF
 */

import java.util.Scanner;

public class Ass4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter Basic Salary: ");
		double b_sal=sc.nextDouble();
		double hra=b_sal*0.15;
		double da=b_sal*0.30;
		double pf=b_sal*0.125;
		double g_sal=b_sal+hra+da;
		double n_sal=g_sal-pf;
		System.out.println("Net Salari= "+n_sal);
	}

}
