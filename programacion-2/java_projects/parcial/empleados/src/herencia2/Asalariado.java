package herencia2;

public class Asalariado extends Empleado {
      private double sueldo;

	public Asalariado(String nombre, String apellido, String legajo, double sueldo) {
		super(nombre, apellido, legajo);
		this.sueldo = sueldo;
	}

	public double getSueldo() {
		return sueldo;
	}

	public void setSueldo(double sueldo) {
		this.sueldo = sueldo;
	}
	public String toString()
	{
		return super.toString()+", "+ "sueldo: "+ calcSueldo();
	}
    public double calcSueldo()
    {
    	return sueldo;
    }
}
