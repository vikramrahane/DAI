package com.DAI;

import java.util.HashMap;
import java.util.HashSet;
import java.util.*;
import java.util.Map;
import java.util.Set;

public class UtilityReport {
	private Map<String,Double> m;
	public void showReport()
	{
		
	}
	public void createMap()
	{
		m=new HashMap<>();
		UtilityList ul=new UtilityList()			;
		ul.createList();
		for(Student s:ul.getStudList())
		{
			m.put(s.getName(),s.getPercentage());
		}
		
		
	}
	public void printMap()
	{
		Set<String> stud=m.keySet();
		for(String keys:stud)
		{
			System.out.println(keys+"-->"+m.get(keys));
		}
	}
}
