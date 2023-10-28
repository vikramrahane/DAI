import java.util.*;

public class Ass1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Set<Vehicle> vehlist=new HashSet<Vehicle>();
		Scanner sc=new Scanner(System.in);
		int ch;
		do
		{
			System.out.println("1.Add Vehicle\n2.Display All Vehicles\n3.Max & Min Cost Vehicle");
			System.out.println("4.Exit\nEnter your choice: ");
			ch=sc.nextInt();
			switch(ch)
			{
				case 1:
					Vehicle e=new Vehicle();
					e.acceptVehicle();
					vehlist.add(e);
					break;
				case 2:
					System.out.println("Details of All Vehicles: ");
					for(Vehicle val:vehlist)   // Using for-each loop
					{
						val.printVehicle();
					}
					break;
				case 3:
					System.out.println("\nDetails of MAx & Min Cost Vehicles: \n");
					Set<Vehicle> sorted=new TreeSet<Vehicle>();
					sorted.addAll(vehlist);
					
					Vehicle[] varr=new Vehicle[sorted.size()];
					sorted.toArray(varr);

					System.out.println("Minimum Cost Vehicle. ");
					varr[0].printVehicle();
					System.out.println("Maximum Cost Vehicle. ");
					varr[varr.length-1].printVehicle();
					break;
				case 4:
					System.exit(0);
				default:
					System.out.println("You Enter a wrong choice.");
			}
		}while(ch!=4);
	}

}
