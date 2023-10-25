// Exception - It is defined as run time anomaly 
public class Tester {

	public static void main(String[] args){
		// TODO Auto-generated method stub
		try {
			System.out.println("Start");
			f1();
			System.out.println("End");
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public static void f1() throws InterruptedException {
		f2();
	}
	public static void f2() throws InterruptedException {
		f3();
	}
	public static void f3() throws InterruptedException {
		
		Thread.sleep(2000);
		//throw new InterruptedException();
	}

}
