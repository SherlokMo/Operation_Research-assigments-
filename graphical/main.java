import java.util.*;
class lpp
{
   public static void main(String args[])
   {
        Scanner sc = new Scanner(System.in);
	System.out.println("Example of the Question.");
        System.out.println("Solve the LPP by graphical method.");
	System.out.println("Max Z = 3x1+4x2  [Object Function]");
	System.out.println("Subject To  x1+2x2<=4  [1st Set of Constant]");
	System.out.println("           3x1+2x2<=6  [2nd Set of Constant]");
	System.out.println("            x1,x2>=0   [Non -ve restriction]");
	System.out.println("if Objective function symbol x1 or x2 or x3 then enter x1");
	System.out.println("if Objective function symbol x or y or z then enter x");
	System.out.println("Example Max Z = 3x1+4x2 then enter x1");
	System.out.println("Example Max Z = 3x+4y then enter x");
	System.out.println("Enter Objective function symbol : ");
	String s=sc.next();
	System.out.println("Example Max Z = 7x1+12x2 then value of objective function value is 7 12");
	System.out.println("Example Max Z = 3x1+4x2 then value of objective function value is 3 4");
	System.out.println("Enter value of objective function value");
	int z1=sc.nextInt();
	int z2=sc.nextInt();
	StringBuffer x11=new StringBuffer("");
	StringBuffer x12=new StringBuffer("");
	if(s.equals("x1"))
	    {
		x11=x11.append("x1");
		x12=x12.append("x2");
	    }
	else if(s.equals("x"))
	    {
		x11=x11.append("x");
		x12=x12.append("y");
	    }
	System.out.println("Enter 1st Set of Constant means question is x1 +2x2 <=4 then enter 1 2 4");
	int a=sc.nextInt();
	int b=sc.nextInt();
	int c=sc.nextInt();
	System.out.println("Enter 2st Set of Constant means question is 3x1 +2x2 <=6 then enter 3 2 6");
	int f=sc.nextInt();
	int g=sc.nextInt();
	int h=sc.nextInt(); 
	System.out.println("\nstep-1");
	System.out.println("-------");
	System.out.println("Convert all the inequalities in to equations.");
	System.out.println("        "+a+x11+" + "+b+x12+"="+c+" ---equation -1");
	System.out.println("        "+f+x11+" + "+g+x12+"="+h+" ---equation -2");
	System.out.println("\nstep-2");
	System.out.println("-------");
	System.out.println("Find the co-ordinates of the equations.");
	System.out.println("       "+a+x11+" + "+b+x12+"="+c+" ---equation -1");
	int d=c/b;
	int e=c/a;
	System.out.println("         ---------------");
	System.out.println("         | "+x11+" | 0 | "+e+" |");
	System.out.println("         | "+x12+" | "+d+" | 0 |");
	System.out.println("         ---------------");
	System.out.println("Eqn(1) passing through the points(0,"+d+") and ("+e+",0).");
	System.out.println("\n Similarly, consider the eqn(2)");
	System.out.println("       "+f+x11+" + "+g+x12+"="+h+" ---equation -2");
	int d1=h/g;
	int e1=h/f;
	System.out.println("         ---------------");
	System.out.println("         | "+x11+" | 0 | "+e1+" |");
	System.out.println("         | "+x12+" | "+d1+" | 0 |");
	System.out.println("         ---------------");
	System.out.println("Eqn(2) passing through the points(0,"+d1+") and ("+e1+",0).");
        System.out.println("\nStep-3");
        System.out.println("-------");	
	System.out.println("\n Plot the graph:");
	System.out.println("User create own graph computer can't create graph but calculate graph points and values");
	int a11,a12,c11,c12;
	if(e1<e)
	    {
	        a11=e1;
	    }
	else
	   {
	       a11=e;		
	   }
	if(d1<d)
	   {
	       c12=d1;
	   }
	else
	   {
              c12=d;		
	   }
	System.out.println("Hence the feasible region is 0ABC , Where ");
	System.out.println("      0(0,0)");
	System.out.println("      A("+a11+",0)");
	System.out.println("      B("+x11+","+x12+")");
	System.out.println("      c(0,"+c12+")");
        System.out.println("\nStep-4");
        System.out.println("-------");	
        System.out.println("   Solve for co-ordinates 'B'");	
        System.out.println("   --------------------------");	
 	int a1=a*g;
	int b1=b*g;
	int c1=c*g;
	int f1=f*b;
	int g1=g*b;
	int h1=h*b;
	System.out.println("     Eqn(1)*"+f+"   "+a1+x11+" + ("+b1+x12+")="+c1);
	System.out.println("     Eqn(2)*"+a+"   "+f1+x11+" + ("+g1+x12+")="+h1);
        System.out.println("            (-)------------");
	int i=a1-f1;
	int j=c1-h1;
	float x1=j/i;
	System.out.println("                "+i+x11+" = "+j);
	System.out.println("\n                  "+x11+" = "+x1+"\n");
	System.out.println(x11+" value put into eqn(1)");
	System.out.println("   "+a*x1+" + "+b+x12+" = "+c);
	float x2=(c-(a*x1))/b;
        System.out.println("\n   "+x12+"="+x2);
	System.out.println("\n   b("+x11+","+x12+")=("+x1+","+x2+")");
	System.out.println("\n Find the optimal solution.");
	System.out.println("---------------------------");
	float za=z1*a11;
	float zb=z1*x1+z2*x2;
	float zc=z2*c12;
	float max=(za>zb)?(za>zc)?za:zc:(zb>zc)?zb:zc;
	float max1=0,max2=0;
	char cc=0;
	System.out.println("      Corner            Value of objective");
	System.out.println("      Points            function=Z="+z1+x11+" +"+z2+x12);
	System.out.println("      -------------------------------------");
	System.out.println("      0(0,0)                 Z0 = 0");
	if(za==max)
	{System.out.println("      A("+a11+",0)              ZA="+za+"(Max)");         max1=a11;max2=0;cc='A';}
	else
        {System.out.println("      A("+a11+",0)                 ZA="+za);}
	if(zb==max)
	{System.out.println("      B("+x1+","+x2+")             ZB="+zb+"(Max)");
        max1=x1;max2=x2;cc='B';}
	else
	{System.out.println("      B("+x1+","+x2+")             ZB="+zb);}
	if(zc==max)
	{System.out.println("      c(0,"+c12+")                 ZC="+zc+"(Max)");
        max1=0;max2=c12;cc='C';}
	else
	{System.out.println("      c(0,"+c12+")                 ZC="+zc);}
        System.out.println("Hence, We have got optimal solution at the point"+cc+"("+max1+","+max2+").");
	System.out.println("Thus the solution of the LPP is given by");
	System.out.println("     -----------------");
	System.out.println("     |    "+x11+"="+max1+"\t|");
	System.out.println("     |    "+x12+"="+max2+"\t|");
	System.out.println("     | Max Z="+max+"\t|");
	System.out.println("     -----------------");
	System.out.println("-> The given LPP has unique optimal solution.");
    }
}