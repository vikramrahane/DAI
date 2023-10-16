import java.util.Scanner;

public class array {
	public static void main(String[] args) {
		int[] a= {10,20,30,40,50};
		int[] b= new int[] {5,4,3,2,1};
		int[] c = new int[7];
		
		Scanner sc=new Scanner(System.in);
		for(int i=0;i<c.length;i++)
			c[i]=sc.nextInt();
		
		System.out.println("Array");
		for (int i=0;i<c.length;i++)
			System.out.println(c[i]+" ");
		
		for(int val:c)
		{
			System.out.println(val+" ");
		}

	}
}
