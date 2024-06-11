//Se pide implementar en Java la clase VídeoClub con la siguiente funcionalidad:
//        • Atributos: cuatro listas enlazadas (LinkedList), cada una para almacenar las películas correspondientes a un género (Drama, Comedia, Suspenso, Musical).
//        • método público añadePelícula: recibe como argumentos la película (objeto de clase Película) y su género.  Añade la película a la lista correspondiente a su género.
//        (si la película ya había sido agregada, escribe un mensaje adecuado).
//        • método privado buscaPelícula: recibe como argumentos el título de la película (String) y su género  y busca la película en la lista correspondiente. Retorna la película buscada (objeto de tipo Película) o null en el caso de que no la encuentre.
//        • método público prestaPelícula: recibe como argumentos el título de la película (String), su género  y el cliente al que se va a prestar la película (objeto de la clase Cliente). Utiliza el método buscaPelícula para buscar la película y, en el caso de que exista, llama al método presta para la película encontrada.
//• En una implementación real la clase VideoClub tendría también métodos para eliminar una película del video club y para anotar que una película prestada ha sido devuelta.
//

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Videoclub {
//    01. ATTRIBUTES
    private LinkedList<Pelicula> drama;
    private LinkedList<Pelicula> comedia;
    private LinkedList<Pelicula> suspenso;
    private LinkedList<Pelicula> musical;

    private List<LinkedList<Pelicula>> peliculas;

//    02. CONSTRUCTOR
    public Videoclub() {
        this.drama = new LinkedList<>();
        this.comedia = new LinkedList<>();
        this.suspenso = new LinkedList<>();
        this.musical = new LinkedList<>();
    }

//    03. SETTERS & GETTERS
    public LinkedList<Pelicula> getDrama() {
        return drama;
    }

    public void setDrama(LinkedList<Pelicula> drama) {
        this.drama = drama;
    }

    public LinkedList<Pelicula> getComedia() {
        return comedia;
    }

    public void setComedia(LinkedList<Pelicula> comedia) {
        this.comedia = comedia;
    }

    public LinkedList<Pelicula> getSuspenso() {
        return suspenso;
    }

    public void setSuspenso(LinkedList<Pelicula> suspenso) {
        this.suspenso = suspenso;
    }

    public LinkedList<Pelicula> getMusical() {
        return musical;
    }

    public void setMusical(LinkedList<Pelicula> musical) {
        this.musical = musical;
    }

    //    04. METHODS
    public void anadePelicula(Pelicula pelicula, String genero) {
        if (genero.equals("drama")) {
            if(drama.isEmpty()) {
                drama.add(pelicula);
            } else {
                for(Pelicula peli : drama) {
                    if(peli.getTitulo().equals(pelicula.getTitulo())) {
                        System.out.printf("El título %s ya está agregado.\n", pelicula.getTitulo());
                    } else {
                        drama.add(pelicula);
                    }
                }
            }
        } else if (genero.equals("suspenso")) {
            if(suspenso.isEmpty()) {
                suspenso.add(pelicula);
            } else {
                for(Pelicula peli : suspenso) {
                    if(peli.getTitulo().equals(pelicula.getTitulo())) {
                        System.out.printf("El título %s ya está agregado.\n", pelicula.getTitulo());
                    } else {
                        suspenso.add(pelicula);
                    }
                }
            }
        } else if (genero.equals("comedia")) {
            if(comedia.isEmpty()) {
                comedia.add(pelicula);
            } else {
                for(Pelicula peli : comedia) {
                    if(peli.getTitulo().equals(pelicula.getTitulo())) {
                        System.out.printf("El título %s ya está agregado.\n", pelicula.getTitulo());
                    } else {
                        comedia.add(pelicula);
                    }
                }
            }
        } else if (genero.equals("musical")) {
            if(musical.isEmpty()) {
                musical.add(pelicula);
            } else {
                for(Pelicula peli : musical) {
                    if(peli.getTitulo().equals(pelicula.getTitulo())) {
                        System.out.printf("El título %s ya está agregado.\n", pelicula.getTitulo());
                    } else {
                        musical.add(pelicula);
                    }
                }
            }
        }

    }

    public void imprimirGenero(String genero) {
        if (genero.equals("drama")) {
            for (Pelicula pelicula : drama) {
                System.out.println(pelicula.getTitulo());
            }
        } else if (genero.equals("suspenso")) {
            for (Pelicula pelicula : suspenso) {
                System.out.println(pelicula.getTitulo());
            }
        } else if (genero.equals("comedia")) {
            for (Pelicula pelicula : comedia) {
                System.out.println(pelicula.getTitulo());
            }
        } else if (genero.equals("musical")) {
            for (Pelicula pelicula : musical) {
                System.out.println(pelicula.getTitulo());
            }
        }
    }

//
    private Pelicula buscaPelicula(String tit, String genero) {
        if (genero.equals("drama")) {
            for (Pelicula peli : drama) {
                if (tit.equals(peli.getTitulo())) {
                    return peli;
                }
            }
        } else if (genero.equals("musical")) {
            for (Pelicula peli : musical) {
                if (tit.equals(peli.getTitulo())) {
                    return peli;
                }
            }
        } else if (genero.equals("comedia")) {
            for (Pelicula peli : comedia) {
                if (tit.equals(peli.getTitulo())) {
                    return peli;
                }
            }
        } else if (genero.equals("suspenso")) {
            for (Pelicula peli : musical) {
                if (tit.equals(peli.getTitulo())) {
                    return peli;
                }
            }
        }
        return null;
    }

    public void prestaPelicula(String titulo, String genero, Cliente cliente) {
        Pelicula peliculaPrestar = buscaPelicula(titulo,genero);
        if (peliculaPrestar != null) {
                peliculaPrestar.presta(cliente.getNombre());
                System.out.printf("La película %s del género %s ha sido prestada al cliente %s\n", titulo, genero, cliente.getNombre());
            }
    }

    public void devolverPelicula(String titulo, String genero, Cliente cliente) {
        if (genero.equals("drama")) {
            for(Pelicula peli : drama) {
                if (titulo.equals(peli.getTitulo())) {
                    peli.setPrestada(false);
                }
        }
        }
        System.out.printf("La película %s del género %s ha sido devuelta al videoclub por el cliente %s\n", titulo, genero, cliente.getNombre());
    }

    public void eliminarPelicula(String nombre, String genero) {
        if(genero.equals("drama")) {
            for(Pelicula peli : drama) {
                if (peli.getTitulo().equals(nombre)) {
                    drama.remove(peli);
                    System.out.printf("Se ha eliminado la película %s del género %s\n",nombre,genero);
                }
            }
        }
    }
}
