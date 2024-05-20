package piezas;

public class Rey  extends Pieza{

	public Rey(int x, int y) {
		super(x,y,"Rey");
	}

	@Override
	public boolean mover(int x, int y) {
		boolean aux = false;
		int absx = Math.abs(this.x - x);
		int absy = Math.abs(this.y - y);
		if ((absx == 1 && absy == 1) || ( absx == 1 && this.y == y) || (absy == 1 &&  this.x == x))
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
		return mover(r.getX(), r.getY());
	}
	

}
