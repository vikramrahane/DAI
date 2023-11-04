import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class GroceryList {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<GroceryItem> grocery_list=new ArrayList<GroceryItem>();
		Scanner sc=new Scanner(System.in);
		DateTimeFormatter date_only = DateTimeFormatter.ofPattern("dd-MM-yyyy");
		do
		{
			System.out.println("1.Add New Item\n2.Update Stock\n3.Display All\n4.Remove all empty stock items");
			System.out.println("5.Last Updated Stock Items(Last 3 Days Only)\n6.Exit");
			System.out.println("Enter your choice");
			int ch=sc.nextInt();
			switch(ch)
			{
				case 1:
					System.out.println("Enter Item Name: ");
					String s=sc.next();				
					System.out.println("Enter Item Price Per Unit: ");
					double price=sc.nextDouble();
					System.out.println("Enter Quantity: ");
					int qty=sc.nextInt();
					
					
					GroceryItem itm=new GroceryItem();
					itm.setItem_name(s);
					itm.setPrice_per_unit(price);
					itm.setStock_qty(qty);
					LocalDateTime dt=LocalDateTime.now();
					DateTimeFormatter dt_format = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
					
					itm.setUpdated_datetime(dt.format(dt_format));
					
					grocery_list.add(itm);
					break;
				case 2:
					System.out.println("Enter Item Name for Stock Modification: ");
					String itmname=sc.next();
					for(int i=0;i<grocery_list.size();i++)
					{
						GroceryItem gitm=grocery_list.get(i);
						if(itmname.equalsIgnoreCase(gitm.getItem_name()))
						{
							int cur_stock=gitm.getStock_qty();
							System.out.println("Enter Quantity: ");
							int sqty=sc.nextInt();
							int total=gitm.getStock_qty()+sqty;
							gitm.setStock_qty(total);
							LocalDateTime udt=LocalDateTime.now();
							DateTimeFormatter udt_format = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
							
							gitm.setUpdated_datetime(udt.format(udt_format));
						}
						else if(i==grocery_list.size()-1)
						{
							System.out.println("Item not Found in the List.");
						}
					}
					break;
				case 3:
					for(GroceryItem i:grocery_list)
					{
						System.out.println(i);
					}
					break;
				case 4:
					for(int i=0;i<grocery_list.size();i++)
					{
						GroceryItem gitm=grocery_list.get(i);
						if(gitm.getStock_qty()==0)
						{
							grocery_list.remove(i);
						}						
					}
					break;
				case 5:
					dt=LocalDateTime.now();
					LocalDateTime d1=dt.minusDays(1);
					LocalDateTime d2=dt.minusDays(2);
					String today=dt.format(date_only);
					String dt1=d1.format(date_only);
					String dt2=d2.format(date_only);
					for(int i=0;i<grocery_list.size();i++)
					{
						GroceryItem gitm=grocery_list.get(i);
						String old=gitm.getUpdated_datetime();
						String old1=(String) old.subSequence(0, 10);
						System.out.println(old1);
						if(old1.equals(today) || old1.equals(dt1)||old1.equals(dt2))
						{
							System.out.println(gitm);
						}						
					}
					break;
				default:
					
			}
		}while(true);
	}

}
