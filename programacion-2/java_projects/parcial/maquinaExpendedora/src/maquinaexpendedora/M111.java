package maquinaexpendedora;

public class M111 extends Maquina{
       private int te;
       private int leche;
     public M111(int s)
     {
    	 super(s);
    	 te = maxTe;
    	 leche = maxLeche;
     }
	public int getTe() {
		return te;
	}
	
	public int getLeche() {
		return leche;
	}
	public boolean cafeConLeche()
	{
		boolean preparado = false;
		int cantLeche = leche - cantIngredientes[3][1];
		int cantCafe = cafe - cantIngredientes[0][1];
		if (cantLeche >= 0 && cantCafe >= 0)
		{
			leche = cantLeche;
			cafe = cantCafe;
			preparado = true;
		}
		return preparado;
	}
     
}
