import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Tester1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		File file=new File("ppr.txt");
		try {
			file.createNewFile();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("File Created");
		
		  FileWriter filewriter; 
		  try 
		  { 
			  filewriter = new FileWriter(file);
			  filewriter.write("This is first line into the file.   "); 
			  filewriter.close();
		  } catch (Exception e) { // TODO Auto-generated catch block
		  e.printStackTrace(); }
		 
		
		
		/*
		
		  FileReader fr; 
		  try 
		  { 
			  char []s= new char[100];			  
			  fr = new FileReader(file);
			  fr.read(s); 
			  System.out.println(s); 
		  } catch (Exception e) 
		  { // TODO
			  e.printStackTrace(); 
		  }
		 
		*/
		
		
		/*
		  try { Scanner sc= new Scanner(file); while(sc.hasNextLine()) { String s =
		  sc.nextLine(); System.out.println(s); } } catch (FileNotFoundException e) {
		  // TODO Auto-generated catch block e.printStackTrace(); }
		 */
		
			
		
	}

}
