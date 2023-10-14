import java.util.Scanner;
class Ass1
{
	public static void main(String[] args)
	{
		//int a[]=new int[5];
		Scanner sc=new Scanner(System.in);
		double x=1,sum=0;
		for(int i=0;i<5;i++)
		{
			System.out.println("Enter a No: ");
			x=sc.nextInt();
			sum=sum+x;
		}
		double avg=sum/5;
		System.out.println("Average of Given No's is: "+avg);
	}
}
