package figuras;

public class Circulo extends Figura{
	// circulo es una figura (herencia)
     private double radio;
     public Circulo(Punto p, Punto q)
     {
    	 super(p,q);
    	 radio = super.calcDistancia(p,q);
     }
     public void dibujar()
     {
    	 System.out.println("soy un circulo");
     }
     public double area()
     {
    	 return Math.PI * radio * radio;
     }
     public double perim()
     {
    	 return Math.PI * 2 * radio;
     }
     public String toString()
     {
    	 return "radio: "+radio+ ", "+super.toString();
     }
}
