import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.TreeSet;

public class Tester {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Set<Integer> s=new HashSet<Integer>();
		/*
		 */
		s.add(13);
		s.add(10);
		s.add(123);
		s.add(1);
		s.add(15);
		s.add(13);
		s.add(15);
		//s.add(13);
		//s.add(13);
		System.out.println(s);
		System.out.println();
		Set<Integer> ls=new LinkedHashSet <Integer>();
		/*
		 */
		ls.add(13);
		ls.add(10);
		ls.add(123);
		ls.add(1);
		ls.add(15);
		ls.add(13);
		ls.add(15);
		//s.add(13);
		//s.add(13);
		System.out.println(ls);
		System.out.println();
		Set<Integer> ts=new TreeSet<Integer>() ;
		/*
		 */
		ts.add(13);
		ts.add(10);
		ts.add(123);
		ts.add(1);
		ts.add(15);
		ts.add(13);
		ts.add(15);
		//s.add(13);
		//s.add(13);
		System.out.println(ts);
	}

}
