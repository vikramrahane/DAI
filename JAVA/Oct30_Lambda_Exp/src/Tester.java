
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.stream.Stream;

public class Tester {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		A a= new A()
				{
			public void show()
			{
				System.out.println("This is Anonymous inner class..");
			}
			
			};
			a.show();
			
			A b= ()->	System.out.println("This is Lambda syntex..");
			b.show();
			
			List<Integer> list=Arrays.asList(23,100,12,10,1,45);
			list.forEach((x) -> System.out.print(x+"  "));
			
			Stream<Integer> stream= list.stream();
			long cnt=stream.count();
			System.out.println("Numbers of values: "+cnt);
			//stream.forEach((x) -> System.out.print(x+"  "));
			System.out.println();
			list.stream().map((t)->t*2).forEach((t)-> System.out.print(t+"  "));
			System.out.println();
			list.stream().filter((t)->(t%2==1)).forEach((t)-> System.out.print(t+"  "));
	}

} 
