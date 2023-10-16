//4. Write a method “add” to add n number of integers. Use VarArgs
public class Ass4 {
	public static void add(int ...a)
	{
		int sum=0;
		for(int i=0;i<a.length;i++)
		{
			sum=sum+a[i];
		}
		System.out.println("Sum: "+sum);
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		add(1,2,3,4,5,6);
		add(1,2,3);
		

	}

}
