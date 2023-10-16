import java.util.Scanner;
public class array2D {
	public static void main(String[] args) {
		int[][] a= {{1,2,3},{4,5,6},{7,8,9}}; //Initialize 2D array
		int[][] b= {{1,2,3,4},{5,6},{7,8,9}}; //jagged array
		int[][] c= new int[][] {{1,2,3},{4,5,6},{7,8,9}}; //Initialized 2D array
		
		int [][] d=new int[3][];
		d[0]=new int [3];
		d[1]=new int [5];
		d[2]=new int [2];
		
		Scanner sc= new Scanner(System.in);
		System.out.println("Enter array element: ");
		for(int i =0; i<d.length;i++)
		{
			for (int j=0; j<d[i].length; j++)
			{
				d[i][j]=sc.nextInt();
			}
				
		}
		for(int i=0;i<d.length;i++) {
			for(int j=0;j<d[i].length; j++)
			{
				System.out.println(d[i][j]+" ");
			}
			System.out.println();
		}
		for(int []temp:d)
		{
			for(int val:temp)
			{
				System.out.println(val+" ");
			}
			System.out.println();
		}
	}
}
