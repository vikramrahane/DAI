
public class Date1 {

	
		private int dd;
		private int mm;
		private int yy;
		
		
		public Date1() {
			dd=1;
			mm=1;
			yy=2000;
		}


		public Date1(int dd, int mm, int yy) {
			this.dd = dd;
			this.mm = mm;
			this.yy = yy;
		}
		public void show() {
			System.out.println(dd+"/"+mm+"/"+yy);
		}
}
