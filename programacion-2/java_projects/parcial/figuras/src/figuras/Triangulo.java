package figuras;

public abstract class Triangulo extends Figura{
      private Punto r;
      protected double ladoA;
      protected double ladoB;
      protected double ladoC;
      public Triangulo (Punto a, Punto b, Punto c)
      {
    	  super(a,b);
    	  r = c;
    	  ladoA = super.calcDistancia(a,b);
    	  ladoB = super.calcDistancia(a,c);
    	  ladoC = super.calcDistancia(b,c);
      }
      public String toString()
      {
    	  return "triangulo de lados: "+ ladoA+","+ladoB+","+ladoC;
      }
      public double perim()
      {
    	  return ladoA + ladoB + ladoC;
      }
      public double area ()
      {
    	  // formula para euilatero e isosceles. Sobreescibir para escaleno
          double base = ladoB / 2;
          double altura = Math.sqrt(3) * ladoA /2;
          return base * altura /2;
      }
}
