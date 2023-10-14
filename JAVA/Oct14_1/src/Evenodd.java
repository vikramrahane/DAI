
public class Evenodd {

	public static void main(String[] args) {
		int num=11;
		if(num%2==0)	// (if else)
			System.out.println("Even..");
		else
			System.out.println("Odd...");
		
		int n=5, cnt=1;	//syntax for "while"
		while(cnt<=10) {
			System.out.println(n*cnt+" ");
			cnt++;
		}
		System.out.println();
		
		for(int i=1; i<=10; i++)  // syntax for "for"
			System.out.println(n*cnt+" ");
	}

}
