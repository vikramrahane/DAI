
public class Ass2 {

	public static void main(String[] args) throws CloneNotSupportedException
	{
		// TODO Auto-generated method stub
		Vehicle v1=new Vehicle(1969, "Pulsar", 95000);
		Vehicle v2=(Vehicle)v1.clone();
		v2.disp();
	}

}
