
public class Student_Ass_2_3 {


	private static int cnt;
	int rno;
	private String name;
	private double per;
	
	static
	{
		cnt=101;
	}
	public Student_Ass_2_3(String name, double per) {
		
		this.name = name;
		this.per = per;
		this.rno=cnt;
		cnt++;
	}
	public Student_Ass_2_3() {
		this.name = "abc";
		this.per = 0.0;
		this.rno=cnt;
		cnt++;
	}
	@Override
	public String toString() {
		return "Roll No=" +rno+" Student name=" + name + ", per=" + per + "";
	}
	public String getName() {
		return this.name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public double getPer() {
		return this.per;
	}
	public void setPer(double per) {
		this.per = per;
	}
	public int getRno() {
		return this.rno;
	}
	
	
}


