
public class FtPlayer implements Printable {
	private String name;
	private int goals;
	
	public FtPlayer(String name, int goals) {
		super();
		this.name = name;
		this.goals = goals;
	}

	public FtPlayer() {
		this.name = "abc";
		this.goals = 0;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getGoals() {
		return goals;
	}

	public void setGoals(int goals) {
		this.goals = goals;
	}

	@Override
	public void printDetails() {
		// TODO Auto-generated method stub
		System.out.println("Football Player Name: "+name+" Goals: "+goals);
	}

}
