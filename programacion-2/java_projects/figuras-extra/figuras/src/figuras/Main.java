package figuras;

public class Main {

	public static void main(String[] args) {
		Circulo c = new Circulo(new Punto(1,2), new Punto(5,6));
		Figura d = c;
		System.out.println(d);
		Rect r  = new Rect(new Punto(3,5),new Punto(3,3), new Punto(6,3),
				                  new Punto(6,5));
		System.out.println(r);
		d = r;
		System.out.println(d);
		Punto a = new Punto(0,0);
		Punto b = new Punto(2,0);
		Punto s = new Punto(1,1.732);
		Figura v [] = {c, r, new Equilatero(a,b,s)};
        for(int i = 0; i<v.length; i++ )
        	System.out.println(v[i].area());
        Todo dibu = c;
        System.out.println(dibu.area());
	}

}
