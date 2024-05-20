package piezas;

public class Main {
	public static void main(String[] args) {
		Jaqueable pieza = new Alfil(1,1);
		Jaqueable rey = new Rey(4,4);
		System.out.println("jaque: "+ pieza.verificarJaque(rey));
        Jaqueable r = new Rey(4,5);
        System.out.println("jaque: "+ pieza.verificarJaque(r));
        System.out.println("jaque: "+ r.verificarJaque(rey));
        Jaqueable torre = new Torre(3,3);
        System.out.println(torre+ " "+ torre.verificarJaque(rey));
	}
}
