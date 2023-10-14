//Write a program to generate all possible combinations of 1, 2, 3 using for loop.
public class Ass10 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i,j,k;
		/*
		 * for(i=1;i<4;i++) { for(j=1;j<4;j++) { if(j!=i) { for(k=1;k<4;k++) { if(k!=i
		 * && k!=j) { System.out.print(i+""+j+""+k+""); System.out.print(" "); } } } } }
		 */
		
		for(i=1;i<4;i++)
		{
			for(j=1;j<4;j++)
			{
				for(k=1;k<4;k++) 
				{
					if(i!=j && j!=k && k!=i)
						System.out.println(i+" "+j+" "+k+" ");
				}
			}
		}
	}

}
