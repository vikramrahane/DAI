import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Ass1 {
	public static void main(String[] args) {
		File src=new File("src.txt");
		File dest=new File("dest.txt");
		
		try {
			
			dest.createNewFile();
			FileWriter fw=new FileWriter(dest);
			
			Scanner sc=new Scanner(src);
			while(sc.hasNextLine())
			{
				String s=sc.nextLine();
				fw.write("\n"+s);
			}
			fw.close();
			
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}

