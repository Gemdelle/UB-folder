package figuras;

public class Equilatero extends Triangulo{
	public Equilatero (Punto a, Punto b, Punto c)
	{
		super(a,b,c);
	}
    public void dibujar()
    {
    	System.out.println("equilatero");
    }
}
