
public class DivideByZeroExc {
	
	public static double divide(int x,int y) {
		double z;
		
		z=x/y;
		return (double)z;
		
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try
		{
			System.out.println(divide(12,0));
		}
		catch(Exception e)
		{
			e.printStackTrace();
			System.out.println("Error");
		}
	}

}
