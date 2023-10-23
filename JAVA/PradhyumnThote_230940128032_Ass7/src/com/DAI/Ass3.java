package com.DAI;

import java.util.Collections;

public class Ass3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		UtilityList slist=new UtilityList();
		slist.createList();
		slist.printList();
		System.out.println("Sorted Student List According to Percentage: ");
		
		Collections.sort(slist.getStudList(), new StudentSortOnPercentage());
		slist.printList();
	}

}
