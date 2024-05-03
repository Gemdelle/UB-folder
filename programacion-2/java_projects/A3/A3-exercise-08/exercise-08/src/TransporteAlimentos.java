import java.util.ArrayList;

public class TransporteAlimentos extends Transporte{
    // 01. ATTRIBUTES
    private ArrayList<Alimento> alimentos;

    // 02. CONSTRUCTOR
    public TransporteAlimentos(String patente, String descripcion, String salida, String llegada, ArrayList<Alimento> alimentos) {
        super(patente, descripcion, salida, llegada);
        this.alimentos = alimentos;
    }

    //    03. SETTERS & GETTERS
    public ArrayList<Alimento> getAlimentos() {
        return alimentos;
    }

    public void setAlimentos(ArrayList<Alimento> alimentos) {
        this.alimentos = alimentos;
    }

//    04. METHODS
    private int calcularPeso() {
        int pesoTotal = 0;
        for(Alimento alimento : alimentos) {
            int pesoAlimento = alimento.getPeso() * alimento.getCantidad();
            pesoTotal += pesoAlimento;
        }
        return pesoTotal;
    }

    @Override
    public float calcularCostoTotal() {
        int pesoTotal = calcularPeso();
        float pesoKg = calcularPesoKg(pesoTotal);

        return calcularPeso() * pesoKg + calcularEnvio(salida,llegada);
    }
}
