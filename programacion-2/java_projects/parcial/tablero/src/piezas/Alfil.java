package piezas;

public class Alfil extends Pieza {
	
	
	public Alfil(int x, int y) {
		super(x, y, "Alfil");
	}

	@Override
	public boolean mover(int x, int y) {
		boolean aux = false;
		if (Math.abs(this.x - x) == Math.abs(this.y - y))
		{
			this.x = x;
			this.y = y;
			aux = true;
		}
		return aux;
	}

	@Override
	public boolean mover(Jaqueable p) {
	    Pieza r = (Pieza)p;
		return mover(r.getX(),r.getY());
	}

	
}
