import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.Scanner;

public class FileHandler implements Runnable{
	private Thread t1,t2;
	private String s;
	private File src,dest;
	private int cnt1;
	
	public FileHandler(String src, String dest) {
		super();
		this.src = new File(src);
		this.dest = new File(dest);
		t1=new Thread(this);
		t2=new Thread(this);
		t1.start();
		t2.start();
		s="";		
	}	
	@Override
	public void run() {
		FileWriter fw;
		
		try
		{
			FileReader fr=new FileReader(src);
			fw=new FileWriter(dest);
			Scanner sc=new Scanner(src);
		
			if(Thread.currentThread()==t1)
			{
				while(sc.hasNextLine())
				{
					s=s+sc.nextLine()+"\n";									
				}				
			}
			if(Thread.currentThread()==t2)
			{
				Thread.sleep(3000);				
				fw.write(s);
				fw.close();
			}
			
		}
		catch(Exception e)
		{
			e.printStackTrace();
			System.out.println("Error");
		}		
	}

}
