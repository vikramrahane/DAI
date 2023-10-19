
public class Student {
	static int cnt=101;
	private int rno;
	private String name;
	private Date1 dob;
	public Student(String name, int d,int m,int y) {
		super();
		this.rno = cnt;
		this.name = name;
		this.dob = new Date1(d,m,y);
		cnt++;
	}
	public Student() {
		super();
		this.rno = cnt;
		this.name = "abc";
		this.dob = new Date1(1,1,2000);
		cnt++;
	}
	public void show()
	{
		System.out.println("Student Name: "+this.name+" Roll No: "+this.rno);
		System.out.println(" Date of Birth: ");
		this.dob.show();
	}
	

}
