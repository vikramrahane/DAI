import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class Tester1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		File file= new File("xyz.dat");
		FileOutputStream fos;
		try {
			fos = new FileOutputStream(file);
			ObjectOutputStream cos= new ObjectOutputStream(fos);
			cos.writeObject(new Laptop(101,"hp",35000));
			cos.writeObject(new Laptop(102,"dell",40000));
			cos.close();
			fos.close();
			System.out.println("object is saved");
			
		}
		catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		FileInputStream fis;
		try {
			fis = new FileInputStream(file);
			ObjectInputStream ois=new ObjectInputStream(fis);
			Laptop l1=(Laptop)ois.readObject();
			System.out.println(l1);
			Laptop l2=(Laptop)ois.readObject();
			System.out.println(l2);
			ois.close();
			fis.close();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
	}

}
