/*2. Write a program to accept and display 3 by 3 matrix. Use enhanced for loop for display.
a. Find the transpose of a matrix and print the transpose.
b. Accept another matrix of same dimensions. Find the addition of two matrices and print the
resultant matrix.*/
public class Ass2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] a=new int[][] {{1,2,3},{4,5,6},{7,8,9}};
		int[][] trans_a=new int[3][3];
		for(int[] i:a)
		{
			for(int val:i)
			{
				System.out.print(val+" ");
			}
			System.out.println();
		}
		
		for(int i=0;i<a.length;i++)
		{
			for(int j=0;j<a[i].length;j++)
			{
				if(i<j || i>j)
				{
					trans_a[i][j]=a[j][i];
				}
				if(i==j)
				{
					trans_a[i][j]=a[i][j];
				}
			}
		}
		//Display Transpose of a
		System.out.println("Transpose of a: ");
		for(int[] i:trans_a)
		{
			for(int val:i)
			{
				System.out.print(val+" ");
			}
			System.out.println();
		}
		//Display Transpose of a
		System.out.println("Addition of two Matrices a & trans_a: ");
		int[][] res=new int[3][3];
		for(int i=0;i<3;i++)
		{
			for(int j=0;j<3;j++)
			{
				res[i][j]=trans_a[i][j]+a[i][j];
				System.out.print(res[i][j]+" ");
			}
			System.out.println();
		}
	}

}
