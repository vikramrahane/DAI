/*
 * Write a program for matchstick game between the computer and the user.  Your program should 
 * ensure that the computer always wins. Rules for the game are as follows:				
 * a. There are 21 matchsticks									
 * b. The computer asks the player to pick 1, 2, 3, or 4 matchsticks.					
 * C. Player is given the chance to pick the sticks first then the computer picks the sticks.		
 * d. Whoever is forced to pick up the last matchstick loses the game.
 */

import java.util.Scanner;

public class Ass11 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n=21;
		try (Scanner sc = new Scanner(System.in)) {
			while(n>0)
			{
				
				System.out.print("Pick the Sticks: ");
				int st=sc.nextInt();
				if(st==1 || st==2 ||st==3||st==4)
				{
					n=n-st;
					System.out.println("You Pick "+st+"sticks. Remaining Sticks are :"+(n));
					int c_st=5-st;
					n=n-c_st;
					System.out.println("Computer Pick "+c_st+"sticks.Remaining Sticks are :"+n);
					if(n==1)
					{
						System.out.println("You loss the game. Last stick remaining");
						break;
					}
				}
				else
				{
					System.out.println("Pick Only 4 or less than 4 sticks.");
				}
			}
		}

	}

}
