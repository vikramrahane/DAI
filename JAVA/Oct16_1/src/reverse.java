import java.util.Scanner;
public class reverse {

	public static void main(String[] args) {
		int temp;
		Scanner sc= new Scanner(System.in);
		
		System.out.println("Enter array size: ");
		int []a=new int[sc.nextInt()];
		
		System.out.println("Enter Array element: ");
		for(int i=0;i<a.length;i++)
			a[i]=sc.nextInt();
		
		for(int i=0;i<a.length/2;i++)
		{
			temp=a[i];
			a[i]=a[a.length-i-1];
			a[a.length-i-1]=temp;
		}
		for(int val:a)
			System.out.println(val+" ");
				
		System.out.println();
	}

}
