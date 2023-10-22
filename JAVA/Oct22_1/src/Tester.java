import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class Tester {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Integer> l=new ArrayList<Integer>();
		l.add(2);
		l.add(45);
		l.add(89);
		l.add(12);
		System.out.println(l);
		
		List<Integer> ll=new LinkedList<Integer>(); //Doublly Linked List
		ll.add(21);
		ll.add(451);
		ll.add(891);
		ll.add(121);
		System.out.println(ll);
		
		Collections.sort(l);
		System.out.println(l);
		List<Laptop> laptop_list=new ArrayList<Laptop>();
		laptop_list.add(new Laptop(101,"HP",12000,3));
		laptop_list.add(new Laptop(12,"dell",2000,4));
		laptop_list.add(new Laptop(103,"lenovo",3000,2));
		
		for(Laptop lap:laptop_list)
		{
			lap.disp();
		}
		Collections.sort(laptop_list); //sort on cost (default criteria)
		System.out.println();
		for(Laptop lap:laptop_list)
		{
			lap.disp();
		}
		//By implementing Comparator<Laptop> Interface in class CompareLaptop
		Collections.sort(laptop_list,new CompareLaptop()); //sort on 'srno' (criteria change)
		System.out.println();
		for(Laptop lap:laptop_list)
		{
			lap.disp();
		}
		//By implementing Comparator<Laptop> Interface in class Sort_LaptopRamSize
		Collections.sort(laptop_list,new Sort_LaptopRamSize());//sort on 'ram' (criteria change)
		System.out.println();
		for(Laptop lap:laptop_list)
		{
			lap.disp();
		}
	}

}
