import java.util.Comparator;

public class CompareLaptop implements Comparator<Laptop> {

	@Override
	public int compare(Laptop o1, Laptop o2) {
		// TODO Auto-generated method stub
		if(o1.getSrno()>o2.getSrno())
		{
			return 1;
		}
		else if(o1.getSrno()<o2.getSrno())
		{
			return -1;
		}
		else
			return 0;
	}
	

}
