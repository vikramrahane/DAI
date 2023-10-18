
public class Ass2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		WageEmployee e1=new WageEmployee(101, "Prada", 14, 11, 1998,60,400);
		
		e1.show();
		e1.cal_salary();
		
		SalesPerson s1=new SalesPerson(201, "Viki", 12, 04, 2001, 55, 500, 12, 5);
		
		s1.show();
		s1.cal_salary();
	}

}
