package com.cdac;

public class Product {
	private int pid;
	private String name;
	public int getPid() {
		return pid;
	}
	public void setPid(int pid) {
		
		this.pid = pid;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		
		this.name = name;
	}
	@Override
	public String toString() {
		return "Product [pid=" + pid + ", name=" + name + "]";
	}
	public Product(int pid, String name) {
		super();
		this.pid = pid;
		this.name = name;
	}
	public Product() {
		super();
		this.pid = 1;
		this.name = "";
	}
	public void fn()
	{
		System.out.println("Product is purchased.");
	}
	
}
