
public class MyException extends Exception {

	String message;
	
	public MyException(String message) {
		super();
		this.message = message;
	}

	public String toString() {
		return message;
	}
	
}
