package piezas;
    
public abstract class Pieza  implements Jaqueable {
	
protected int x, y;	
protected String nombrePieza;


public Pieza(int x, int y, String nombrePieza) {
	this.x = x;
	this.y = y;
	this.nombrePieza = nombrePieza;
}


public int getX() {
	return x;
}
public int getY() {
	return y;
}

public void setX(int x) {
	this.x = x;
}

public void setY(int y) {
	this.y = y;
}
public String getNombrePieza() {
	return nombrePieza;
}


public void setNombrePieza(String nombrePieza) {
	this.nombrePieza = nombrePieza;
}

public String toString()
{
	return nombrePieza+": "+x + ", "+ y;
}
@Override
public boolean verificarJaque(Jaqueable r) {
	return mover(r);
}

}
