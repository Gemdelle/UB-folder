package figuras;

public class Escaleno extends Triangulo {
      public Escaleno(Punto a, Punto b, Punto c)
      {
    	  super(a,b,c);
      }
      public void dibujar()
      {
    	  System.out.println("escaleno");
      }
      public double area()
      {
    	  double s = (ladoA+ladoB+ladoC)/2;
    	  return Math.sqrt(s*(s-ladoA)*(s-ladoB)*(s-ladoC));
      }
}
