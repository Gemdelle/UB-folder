package figuras;

public class Rect extends Figura {
     private Punto t;
     private Punto r;
     private double alto;
     private double ancho;
     public Rect (Punto a, Punto b, Punto c, Punto d)
     {
    	 super(a,b);
    	 t = c;
    	 r = d;
    	 alto = super.calcDistancia(a,b);
    	 ancho = super.calcDistancia(c, b);
     }
     public String toString()
     {
    	 return "base: "+ ancho+ ", "+ "altura: "+alto;
     }
	@Override
	public double area() {
		// TODO Auto-generated method stub
		return ancho*alto;
	}
	@Override
	public double perim() {
		// TODO Auto-generated method stub
		return 2*alto+2*ancho;
	}
	@Override
	public void dibujar() {
		System.out.println("soy un rectangulo");
		
	}
     
}
