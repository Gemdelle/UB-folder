package piezas;

public class Torre extends Pieza{

	public Torre(int x, int y) {
		super(x, y, "Torre");
	}

	@Override
	public boolean mover(int x, int y) {
		boolean aux = false;
		if (this.x == x || this.y == y)
		{
			this.x =x;
			this.y= y;
			aux= true;
		}
		return aux;
	}

	@Override
	public boolean mover(Jaqueable p) {
		Pieza r = (Pieza)p;
		return mover(r.getX(),r.getY());
	}

}
