package com.cdac.pack1;

public class Student {
	int rollno;
	String name;
	public int getRollno() {
		return rollno;
	}
	public void setRollno(int rollno) {
		this.rollno = rollno;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Student(int rollno, String name) {
		
		this.rollno = rollno;
		this.name = name;
	}
	public Student() {
		
	}
	public void display()
	{
		System.out.println("Student Name: "+this.name+" Roll No: "+this.rollno);
	}
	
}
