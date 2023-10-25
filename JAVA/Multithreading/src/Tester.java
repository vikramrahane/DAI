
public class Tester {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FirstThread ft=new FirstThread();
		SecondThread st = new SecondThread();
		ft.start();
		st.start();
	}

}
