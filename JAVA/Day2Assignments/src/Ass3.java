/*
 * 3. Write a program which will calculate multiplication of two 3 by 3 matrices.
 */
import java.util.Scanner;
public class Ass3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc=new Scanner(System.in);
		int[][] a=new int[3][3];
		int[][] b=new int[3][3];
		int[][] c=new int[3][3];
		System.out.println("Enter value for Matrix A: ");
		for(int i=0;i<a.length;i++)
		{
			for(int j=0;j<a[i].length;j++)
			{
				System.out.println("Enter value: ");
				a[i][j]=sc.nextInt();				
			}			
		}
		System.out.println("Enter value for Matrix B: ");
		for(int i=0;i<b.length;i++)
		{
			for(int j=0;j<b[i].length;j++)
			{
				System.out.println("Enter value: ");
				b[i][j]=sc.nextInt();				
			}				
		}
		for(int i=0;i<3;i++)
		{
			for(int j=0;j<3;j++)
			{
				int sum=0;
				for(int k=0;k<3;k++)
				{
					sum=sum+(a[i][k]*b[k][j]);
				}
				c[i][j]=sum;
			}			
		}
		System.out.println("Matrix A: ");
		for(int[] i:a)
		{
			for(int val:i)
			{
				System.out.print(val+" ");
			}
			System.out.println();
		}
		System.out.println("Matrix B: ");
		for(int[] i:b)
		{
			for(int val:i)
			{
				System.out.print(val+" ");
			}
			System.out.println();
		}
		System.out.println("Multiplication of A & B: ");
		for(int[] i:c)
		{
			for(int val:i)
			{
				System.out.print(val+" ");
			}
			System.out.println();
		}
	}
}
