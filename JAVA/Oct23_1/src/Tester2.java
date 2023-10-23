import java.util.*;
public class Tester2 {

	public static void main(String[] args) {
		Map<Integer, String> map=new HashMap<>();
		
		map.put(101,"Maths");
		map.put(105,"Science");
		map.put(104,"English");
		
		System.out.println(map);
		Set<Integer> s= map.keySet();
		for (Integer keys:s) {
			System.out.println(keys+" "+map.get(keys));
		}
	}

}
