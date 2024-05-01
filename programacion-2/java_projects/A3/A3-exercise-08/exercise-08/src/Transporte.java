import java.util.ArrayList;

public abstract class Transporte {
    // 01. ATTRIBUTES
    protected String patente;
    protected String descripcion;
    protected String salida;
    protected String llegada;

    // 02. CONSTRUCTOR
    public Transporte(String patente, String descripcion, String salida, String llegada) {
        this.patente = patente;
        this.descripcion = descripcion;
        this.salida = salida;
        this.llegada = llegada;
    }

    // 03. SETTERS & GETTERS
    public String getPatente() {
        return patente;
    }

    public void setPatente(String patente) {
        this.patente = patente;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public String getSalida() {
        return salida;
    }

    public void setSalida(String salida) {
        this.salida = salida;
    }

    public String getLlegada() {
        return llegada;
    }

    public void setLlegada(String llegada) {
        this.llegada = llegada;
    }

    // 03. METHODS
    public float calcularPeso(ArrayList<Float> lista) {
        float pesoTotal = 0;
        for(Float peso : lista) {
            pesoTotal += peso;
        }

        return pesoTotal;
    }
}
