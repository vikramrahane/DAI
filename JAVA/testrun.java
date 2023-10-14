import java.util.Scanner;
class testrun
{
	public static void main(String [] args)
	{
		int a,b;
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter Two number.");
		a=sc.nextInt();
		b=sc.nextInt();
		
		int c=a+b;
		System.out.println("Sum=  "+c);
	}
}
