package herencia2;

public class Main {
//
//	public static void main(String[] args) {
//		Empleado e = new Empleado("pepe","garcia", "12345");
//		System.out.println(e);
//		Asalariado a = new Asalariado("juan","vazquez","45678",1234.90);
//		System.out.println(a);
//        System.out.println("sueldo de juan: "+a.calcSueldo());
//        EmpleadoComision c = new EmpleadoComision(e,10,2000);
//        System.out.println(c);
//        EmpleadoBase b = new EmpleadoBase(c,1000000);
//        System.out.println(b);
//	}
	public static void main(String[] args) {
		Empleado [] nomina  = {
				 new Asalariado("juan","vazquez","45678",1234.90),
				 new EmpleadoComision("pepe","garcia", "12345",10,2000),
				 new EmpleadoBase("pepe","garcia", "12345",10,2000,1000000),
				 new EmpleadoHoras("milagros","De Castro", "13579",1000,10,100)
		};
		Empleado e;
		for(int i = 0; i<nomina.length; i++ ) {
			e = nomina[i];
			System.out.println(e);
	   }
	}
}
