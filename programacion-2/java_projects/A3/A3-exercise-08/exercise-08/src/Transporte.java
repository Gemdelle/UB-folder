import java.util.ArrayList;

public abstract class Transporte implements Transportable {
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
    public abstract float calcularCostoTotal();

    public float calcularPesoKg(int pesoTotal) {
        float pesoKg = 0;
        if (0<pesoTotal && pesoTotal<1200) {
            pesoKg = 6;
        } else if (1201<pesoTotal && pesoTotal<2400) {
            pesoKg = 5.5f;
        } else if (2401<pesoTotal && pesoTotal<4000) {
            pesoKg = 4.3f;
        } else {
            pesoKg = 3.6f;
        }
        return pesoKg;
    }

    public int calcularEnvio(String salida, String llegada) {
        int indexSalida = ciudades.indexOf(salida);
        int indexLlegada = ciudades.indexOf(llegada);
        return precios[indexSalida][indexLlegada];
    }
}
