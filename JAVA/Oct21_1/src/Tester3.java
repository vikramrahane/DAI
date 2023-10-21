//Collections 
import java.util.*;
public class Tester3 {

	public static void main(String[] args) {
		Vector<Integer> v= new Vector<>();
		System.out.println(v.size()+" "+v.capacity());
		v.add(10);
		v.add(20);
		v.add(30);
		v.add(40);
		v.add(50);
		
		System.out.println(v);// Using toString method
		
		for(Integer val:v)   // Using for-each loop
		{
			System.out.print(val+"  ");
		}
		
		System.out.println();
		Iterator<Integer> itr=v.iterator();  // Using Iterator
		while(itr.hasNext()) {
			System.out.print(itr.next()+"  ");
		}
		
	}

}
