package herencia2;

public abstract class Empleado implements SueldoCalculable {
     protected String nombre;
     protected String apellido;
     protected String legajo;
	public Empleado(String nombre, String apellido, String legajo) {
		this.nombre = nombre;
		this.apellido = apellido;
		this.legajo = legajo;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getApellido() {
		return apellido;
	}
	public void setApellido(String apellido) {
		this.apellido = apellido;
	}
	public String getLegajo() {
		return legajo;
	}
	public void setLegajo(String legajo) {
		this.legajo = legajo;
	}
	public String toString()
	{
		return nombre+ ", "+apellido+", "+legajo ;
	}
}
