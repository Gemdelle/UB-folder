
//Se pretende desarrollar un programa que permita gestionar el préstamo de las películas de un vídeo club. Para ello se dispone de las clase Película. El diseño de Película está dado a continuación:
//public class Película implements Prestable{
//    /** aquí poner los atributos necesarios para la clase Película */
//    /** crea una película en estado no prestada */
//    public Película(String título) {...}
//    /** retorna el título de la película */
//    public String título() {...}
//    /** presta la película al cliente indicado. Método de la Interfaz Prestable*/
//    public void presta(String cliente) {...}
//    /** marca una película prestada como devuelta. */
//    public void devuelve(String cliente) {...}
//}

public class Pelicula implements Prestable{
//    01. ATTRIBUTES
        private String titulo;
        private int duracion;
        private String genero;
        private Boolean prestada;

//        02. CONSTRUCTOR

    public Pelicula(String titulo, int duracion, String genero) {
        this.titulo = titulo;
        this.duracion = duracion;
        this.genero = genero;
        this.prestada = false;
    }

//    03. GETTERS & SETTERS

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public int getDuracion() {
        return duracion;
    }

    public void setDuracion(int duracion) {
        this.duracion = duracion;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public Boolean getPrestada() {
        return prestada;
    }

    public void setPrestada(Boolean estado) {
        this.prestada = estado;
    }

//    04. METHODS
        public String titulo() {
            return titulo;
        }

    @Override
    public void presta(String cliente) {
        prestada = true;
    }

    public void devuelve(String cliente) {
        prestada = false;
    }
}
