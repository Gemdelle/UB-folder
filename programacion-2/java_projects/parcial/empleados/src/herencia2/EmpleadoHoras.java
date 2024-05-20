package herencia2;

public class EmpleadoHoras extends Empleado{
     private double basico;
     private int horas;
     private double valor;
	public EmpleadoHoras(String nombre, String apellido, String legajo, double basico, int horas, double valor) {
		super(nombre, apellido, legajo);
		this.basico = basico;
		this.horas = horas;
		this.valor = valor;
	}
	public double getBasico() {
		return basico;
	}
	public void setBasico(double basico) {
		this.basico = basico;
	}
	public int getHoras() {
		return horas;
	}
	public void setHoras(int horas) {
		this.horas = horas;
	}
	public double getValor() {
		return valor;
	}
	public void setValor(double valor) {
		this.valor = valor;
	}
	public double calcSueldo()
	{
		return basico + horas * valor;
	}
    public String toString()
    {
    	return super.toString()+ "sueldo: "+ calcSueldo();
    }
}
