package maquinaexpendedora;

public class Main {
        public static void main(String[] args) {
			Maquina m = new M111(1111);
			
			System.out.println("cafe solo: "+ m.cafeSolo());
			System.out.println("deposito: "+ m.getCafe());
			m = new R101(2222);
		}
}
