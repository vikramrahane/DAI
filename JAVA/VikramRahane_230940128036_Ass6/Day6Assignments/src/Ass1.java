import java.util.Scanner;
import java.util.Vector;

public class Ass1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Vector<Employee> v=new Vector<Employee>();
		Scanner sc=new Scanner(System.in);
		int ch;
		do
		{
			System.out.println("1.Add Employee\n2.Modify Employee by ID\n3.Display All Employee");
			System.out.println("4.Exit\nEnter your choice: ");
			ch=sc.nextInt();
			switch(ch)
			{
				case 1:
					Employee e=new Employee();
					e.accept_emp();
					v.add(e);
					break;
				case 2:
					System.out.println("Enter ID of Employees: ");
					int id=sc.nextInt();
					for(int i=0;i<v.size();i++)
					{
						Employee e1=v.get(i);
						if(e1.getId()==id)
						{
							System.out.println("Enter Name: ");
							e1.setName(sc.next());
							System.out.println("Enter Salary: ");					
							e1.setSal(sc.nextDouble());
							System.out.println("Employee Modify Successfully.");
							break;
						}
					}
					break;
				case 3:
					System.out.println("Details of All Employees: ");
					for(Employee val:v)   // Using for-each loop
					{
						val.disp();
					}
					break;
				case 4:
					System.exit(0);
				default:
					System.out.println("YOu Enter a wrong choice.");
			}
		}while(ch!=4);
	}

}
