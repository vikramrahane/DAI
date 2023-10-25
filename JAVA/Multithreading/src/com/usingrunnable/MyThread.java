package com.usingrunnable;

public class MyThread implements Runnable {
	Thread t1,t2;
	
	public MyThread() {
		super();
		t1=new Thread(this, "t1");
		t2=new Thread(this, "t2");
		t1.start();
		t2.start();
	}

	@Override
	public void run() {
		// TODO Auto-generated method stub
		try {  //Need for sleep()
			for(int i=0;i<10;i++)
			{
				if(Thread.currentThread()==t1)
				{
					//t2.sleep(5000);
					System.out.println("First Thread Running");
				}
				else if(Thread.currentThread()==t2)
				{
					//t2.sleep(10000);
					System.out.println("Second Thread Running");
				}
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}

