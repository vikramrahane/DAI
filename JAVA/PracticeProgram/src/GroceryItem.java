
public class GroceryItem {
	private String item_name;
	private double price_per_unit;
	private int stock_qty;
	private String updated_datetime;
	
	//Constructors
	public GroceryItem(String item_name, double price_per_unit, int stock_qty, String updated_datetime) {
		super();
		this.item_name = item_name;
		this.price_per_unit = price_per_unit;
		this.stock_qty = stock_qty;
		this.updated_datetime = updated_datetime;
	}
	public GroceryItem() {
		super();
	}
	
	//Getters & Setters
	public String getItem_name() {
		return item_name;
	}
	public void setItem_name(String item_name) {
		this.item_name = item_name;
	}
	public double getPrice_per_unit() {
		return price_per_unit;
	}
	public void setPrice_per_unit(double price_per_unit) {
		this.price_per_unit = price_per_unit;
	}
	public int getStock_qty() {
		return stock_qty;
	}
	public void setStock_qty(int stock_qty) {
		this.stock_qty = stock_qty;
	}
	public String getUpdated_datetime() {
		return updated_datetime;
	}
	public void setUpdated_datetime(String updated_datetime) {
		this.updated_datetime = updated_datetime;
	}
	@Override
	public String toString() {
		return "GroceryItem [item_name=" + item_name + ", price_per_unit=" + price_per_unit + ", stock_qty=" + stock_qty
				+ ", updated_datetime=" + updated_datetime + "]";
	}
	
}
