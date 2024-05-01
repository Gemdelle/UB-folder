package figuras;

public abstract class Figura implements Todo {
      //la figura tiene un punto (composición)
	   Punto p;
       Punto q;
       public Figura (int x, int y, int w, int v)
       {
    	   p = new Punto(x,y);
    	   q = new Punto(w,y);
       }
       public Figura(Punto p, Punto q)
       {
    	   this.p = p;
    	   this.q = q;
       }
       private static double pot (double x, double y)
       {
    	   return (x-y)*(x-y);
       }
       public static double calcDistancia(Punto p, Punto q)
       {
    	   return Math.sqrt(pot(p.getX(),q.getX())+pot(p.getY(),q.getY()));
       }
       public String toString()
       {
    	   return p+", "+q;
       }
}
