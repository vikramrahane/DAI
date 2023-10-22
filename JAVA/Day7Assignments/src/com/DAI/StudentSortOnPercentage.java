package com.DAI;

import java.util.Comparator;

public class StudentSortOnPercentage implements Comparator<Student>{

	@Override
	public int compare(Student o1, Student o2) {
		// TODO Auto-generated method stub
		if(o1.getPercentage()>o2.getPercentage())
			return 1;
		else if(o1.getPercentage()<o2.getPercentage())
			return -1;
		else
			return 0;
	}

}
