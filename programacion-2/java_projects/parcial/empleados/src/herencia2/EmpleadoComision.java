package herencia2;

public class EmpleadoComision extends Empleado{
        private double tasa;
        private double ventas;
		public EmpleadoComision(String nombre, String apellido, String legajo, double tasa, double ventas) {
			super(nombre, apellido, legajo);
			this.tasa = tasa;
			this.ventas = ventas;
		}
		public EmpleadoComision(Empleado e, double tasa, double ventas) {
			super(e.nombre,e.apellido,e.legajo);
			this.tasa = tasa;
			this.ventas = ventas;
		}
		public double getTasa() {
			return tasa;
		}
		public void setTasa(double tasa) {
			this.tasa = tasa;
		}
		public double getVentas() {
			return ventas;
		}
		public void setVentas(double ventas) {
			this.ventas = ventas;
		}
        public double calcSueldo()
        {
        	return tasa*ventas;
        }
        public String toString()
        {
        	return super.toString()+ " sueldo: "+ calcSueldo();
        }
}
