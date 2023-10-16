import java.util.Scanner;

public class max_min {
	//public static int pair()
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		
		System.out.println("Enter array size: ");
		int []a=new int[sc.nextInt()];
		
		System.out.println("Enter Array element: ");
		for(int i=0;i<a.length;i++)
			a[i]=sc.nextInt();
		int min=a[0];
		int max=a[0];
		for(int i=0;i<a.length;i++) {
			if(a[i]>max)
				max=a[i];
				
			if(a[i]<min)
				min=a[i];
			    
		}
		System.out.println("maximum is "+max);
		System.out.println("minimum is "+min);

	}

}
