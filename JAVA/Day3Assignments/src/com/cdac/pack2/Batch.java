package com.cdac.pack2;

public class Batch {
	String coursename;
	int strength;
	public String getCoursename() {
		return coursename;
	}
	public void setCoursename(String coursename) {
		this.coursename = coursename;
	}
	public int getStrength() {
		return strength;
	}
	public void setStrength(int strength) {
		this.strength = strength;
	}
	public Batch(String coursename, int strength) {
		
		this.coursename = coursename;
		this.strength = strength;
	}
	public Batch() {
		
	}
	public void display()
	{
		System.out.println("Course Name: "+coursename+" Strength: "+strength);
	}

}
