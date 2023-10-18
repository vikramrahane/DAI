import in.cdac.Date;
import in.cdac.Employee;
import in.cdac.Wageemployee;
public class Tester1 {

	public static void main(String[] args) {
		Employee e1;
		e1= new Employee(1, "Jay", 12,10,2023);
		e1.show();
		//Wageemployee w1;
		e1= new Wageemployee(10, 900, 1, "Vikram", 30, 4, 1991);
		e1.show();
		
		
	}

}
