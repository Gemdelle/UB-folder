package maquinaexpendedora;

import java.util.GregorianCalendar;

public abstract class Maquina implements Maximos{
     protected int serie;
     protected int cafe;
     protected int cacao;
     protected GregorianCalendar fecha;
     public Maquina(int s)
     {
    	 serie = s;
    	 cafe = maxCafe;
    	 cacao = maxCacao;
     }
	public int getSerie() {
		return serie;
	}
	public void setSerie(int serie) {
		this.serie = serie;
	}
	public int getCafe() {
		return cafe;
	}
	
	public int getCacao() {
		return cacao;
	}

	public GregorianCalendar getFecha() {
		return fecha;
	}
	public void setFecha(GregorianCalendar fecha) {
		this.fecha = fecha;
	}
	
    public int reponerCafe(int c)
    {
    	int sobra;
    	if ( cafe + c > maxCafe) {
    		sobra = c - maxCafe;
    		cafe = maxCafe;
    	}
    	else {
    		cafe = cafe + c;
    		sobra = 0;
    	}
    	return sobra;
    }

    public boolean cafeSolo ()
    {
    	boolean preparado = false;
    	int cant = cafe - cantIngredientes[0][0];
    	if (cant >= 0)
    	{
    		preparado = true;
    		cafe = cant;
    	}
    	return preparado;
    }
}
