package herencia2;

public class EmpleadoBase extends EmpleadoComision {
       private double sueldo;

	public EmpleadoBase(String nombre, String apellido, String legajo, double tasa, double ventas, double sueldo) {
		super(nombre, apellido, legajo, tasa, ventas);
		this.sueldo = sueldo;
	}
    public EmpleadoBase (EmpleadoComision e, double sueldo)
    {
    	super(e, 10, 1000);
    	this.sueldo = sueldo;
    }
	public double getSueldo() {
		return sueldo;
	}

	public void setSueldo(double sueldo) {
		this.sueldo = sueldo;
	}
    public double calcSueldo()
    {
    	return super.calcSueldo()+sueldo;
    }
    public String toString()
    {
    	return super.toString();
    }
}
