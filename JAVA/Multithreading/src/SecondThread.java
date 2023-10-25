
public class SecondThread extends Thread {
	public void run() {
		// TODO Auto-generated method stub
		for(int i=0;i<100;i++)
		{
			System.out.println("Second Thread Running");
		}
	}
}
