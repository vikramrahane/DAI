
public class Oct16_4 {
	public static int add(int ...a)
	{
		int sum=0;for (int i=0;i<a.length; i++)
			sum+=a[i];
		return sum;
	}
	public static void main(String[] args)
	{
		System.out.println(add(1,2,3,4,5));//15
		System.out.println(add(1,2,3,4)); //10
	}
}
