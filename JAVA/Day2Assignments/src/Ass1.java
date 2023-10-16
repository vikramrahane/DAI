/*
 * 1. Accept five integers in an array -
a. Find maximum and minimum of the integers. Do not sort the array.
b. Multiply each element of the array by 5 and store it in another array and display it.
 */
import java.util.Scanner;

public class Ass1 {

	public static void main(String[] args) {
			Scanner sc= new Scanner(System.in);
			
			//System.out.println("Enter array size: ");
			int []a=new int[5];
			int []b=new int[5];
			
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
				b[i]=a[i]*5;
				    
			}
			System.out.println("maximum is "+max);
			System.out.println("minimum is "+min);
			for(int i=0;i<a.length;i++) {
				System.out.println(b[i]);
				    
			}
			
		}

}
