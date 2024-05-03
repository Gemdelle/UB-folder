import java.util.ArrayList;
import java.util.Random;

public class TransporteGanado extends Transporte {
//    01. ATTRIBUTES
    int cabezas;
    float pesoPromedio;

//    02. CONSTRUCTOR

    public TransporteGanado(String patente, String descripcion, String salida, String llegada, int cabezas, float pesoPromedio) {
        super(patente, descripcion, salida, llegada);
        this.cabezas = cabezas;
        this.pesoPromedio = pesoPromedio;
    }

//    03. SETTERS & GETTERS

    public int getCabezas() {
        return cabezas;
    }

    public void setCabezas(int cabezas) {
        this.cabezas = cabezas;
    }

    public float getPesoPromedio() {
        return pesoPromedio;
    }

    public void setPesoPromedio(float pesoPromedio) {
        this.pesoPromedio = pesoPromedio;
    }

    //    04. METHODS
    private int calcularPeso() {
        Random random = new Random();
        return cabezas * (random.nextInt(100)+500); // el promedio va a ser un número entre 500 y 600
    }

    @Override
    public float calcularCostoTotal() {
        int pesoTotal = calcularPeso();
        float pesoKg = calcularPesoKg(pesoTotal);

        return calcularPeso() * pesoKg + calcularEnvio(salida,llegada);
    }
}
