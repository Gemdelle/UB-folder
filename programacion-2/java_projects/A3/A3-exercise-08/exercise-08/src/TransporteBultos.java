public class TransporteBultos extends Transporte {
    //    01. ATTRIBUTES
    private int mini;
    private int mid;
    private int max;

//    02. CONSTRUCTOR

    public TransporteBultos(String patente, String descripcion, String salida, String llegada, int mini, int mid, int max) {
        super(patente, descripcion, salida, llegada);
        this.mini = mini;
        this.mid = mid;
        this.max = max;
    }

//    03. SETTERS & GETTERS

    public int getMini() {
        return mini;
    }

    public void setMini(int mini) {
        this.mini = mini;
    }

    public int getMid() {
        return mid;
    }

    public void setMid(int mid) {
        this.mid = mid;
    }

    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }

    //    04. METHODS
    public int calcularPeso() {
        int pesoMini = 10;
        int pesoMid = 50;
        int pesoMax = 75;
        return mini * pesoMini + mid * pesoMid + max * pesoMax;
    }

    @Override
    public float calcularCostoTotal() {
        int pesoTotal = calcularPeso();
        float pesoKg = calcularPesoKg(pesoTotal);

        return calcularPeso() * pesoKg + calcularEnvio(salida,llegada);
    }
}
