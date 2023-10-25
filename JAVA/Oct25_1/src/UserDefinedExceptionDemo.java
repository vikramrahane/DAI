
public class UserDefinedExceptionDemo {
	public static double divide(double x,double y) throws MyException {
		if(y==0)
		{
			throw new MyException("Denomenator is Zero.");
		}
		return x/y;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			System.out.println(divide(12,0));
		} catch (Exception e) {
			// TODO Auto-generated catch block
			System.out.println(e);
		}
	}
}
