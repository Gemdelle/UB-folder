package figuras;

public class Isosceles extends Triangulo{
	public Isosceles (Punto a, Punto b, Punto c)
	{
		super(a,b,c);
	}
    public void dibujar()
    {
    	System.out.println("Isosceles");
    }
    public double area ()
    {
    	double base;
    	double altura;
    	if (ladoA == ladoB)
    		base = ladoC;
    	else if (ladoB == ladoC)
    		   base = ladoA;
    		 else
    		   base = ladoB;
    	altura  = Math.sqrt(3) *  base/2;
    	return base * altura / 2;
    }
}
