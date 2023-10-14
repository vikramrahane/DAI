import java.util.Scanner;

public class Ass1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		int x=1,sum=0;
		for(int i=0;i<5;i++)
		{
			System.out.print("Enter a No: ");
			x=sc.nextInt();
			sum=sum+x;
		}
		double avg=sum/5;
		System.out.println("Average of Given No's is: "+avg);

	}

}
