import java.util.Comparator;

public class Sort_LaptopRamSize implements Comparator<Laptop> {

	@Override
	public int compare(Laptop o1, Laptop o2) {
		// TODO Auto-generated method stub
		if(o1.getRam()>o2.getRam())
		{
			return 1;
		}
		else if(o1.getRam()<o2.getRam())
		{
			return -1;
		}
		else
			return 0;
	}

}
