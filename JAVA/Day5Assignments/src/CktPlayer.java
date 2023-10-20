
public class CktPlayer implements Printable {
	private String name;
	private int runs;
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getRuns() {
		return runs;
	}
	public void setRuns(int runs) {
		this.runs = runs;
	}
	public CktPlayer(String name, int runs) {
		super();
		this.name = name;
		this.runs = runs;
	}
	public CktPlayer() {
		super();
		this.name = "xyz";
		this.runs = 0;
	}
	@Override
	public void printDetails() {
		// TODO Auto-generated method stub
		System.out.println("Cricket Player Name: "+name+" Runs: "+runs);
	}
	
}
