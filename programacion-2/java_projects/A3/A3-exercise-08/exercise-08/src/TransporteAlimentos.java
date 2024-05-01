import java.util.ArrayList;

public class TransporteAlimentos extends Transporte{
    // 01. ATTRIBUTES
    private ArrayList<Alimento> alimentos;

    // 02. CONSTRUCTOR
    public TransporteAlimentos(String patente, String descripcion, String salida, String llegada, ArrayList<Alimento> alimentos) {
        super(patente, descripcion, salida, llegada);
        this.alimentos = new ArrayList<>();
    }

    public ArrayList<Alimento> getAlimentos() {
        return alimentos;
    }

    public void setAlimentos(ArrayList<Alimento> alimentos) {
        this.alimentos = alimentos;
    }
}
