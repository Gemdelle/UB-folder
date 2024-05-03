public class Alimento {
    // 01. ATTRIBUTES
    private int cantidad;
    private int peso;

//    02. CONSTRUCTOR

    public Alimento(int cantidad, int peso) {
        this.cantidad = cantidad;
        this.peso = peso;
    }

//    03. SETTERS & GETTERS

    public int getCantidad() {
        return cantidad;
    }

    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
    }

    public int getPeso() {
        return peso;
    }

    public void setPeso(int peso) {
        this.peso = peso;
    }
}
