
//Se pide realizar la implementación de las clases Pelicula y VideoClub. Realizar una aplicación que permita ingresar una pelicula y prestarla a un cliente.

public class Main {
    public static void main(String[] args) {
//        CREACIÓN DE PELÍCULAS (una de cada género)
        Pelicula pelicula1 = new Pelicula("My friend and I", 160,"drama");
        Pelicula pelicula2 = new Pelicula("Scary Movie", 160,"comedia");
        Pelicula pelicula3 = new Pelicula("IT", 160,"suspenso");
        Pelicula pelicula4 = new Pelicula("Los Miserables", 160,"musical");

//        CREAR VIDEOCLUB Y AGREGAR PELÍCULAS
        Videoclub videoclub = new Videoclub();
        videoclub.anadePelicula(pelicula1, pelicula1.getGenero());
        System.out.println("\n01. VERIFICAR QUE CUANDO SE AGREGA UNA PELÍCULA QUE YA SE HA AGREGADO LO NOTIFICA CON UN MENSAJE");
        videoclub.anadePelicula(pelicula1, pelicula1.getGenero()); // como la película ya está agregada, imprime un mensaje que lo indica

        videoclub.anadePelicula(pelicula2, pelicula2.getGenero());
        videoclub.anadePelicula(pelicula3, pelicula3.getGenero());
        videoclub.anadePelicula(pelicula4, pelicula4.getGenero());

//        IMPRIMIR PELÍCULAS POR GÉNERO
        System.out.println("\n02. IMPRIMIR PELÍCULAS POR GÉNERO");
        System.out.println("DRAMA:");
        videoclub.imprimirGenero("drama");
        System.out.println("SUSPENSO:");
        videoclub.imprimirGenero("suspenso");
        System.out.println("COMEDIA:");
        videoclub.imprimirGenero("comedia");
        System.out.println("MUSICAL:");
        videoclub.imprimirGenero("musical");

//        CREAR CLIENTE
        Cliente cliente1 = new Cliente("Isabella");

//        VERIFICAR EL ESTADO DE PRESTADO DE PELÍCULA 1
        System.out.println("\n03. VERIFICAR ESTADO DE PELÍCULA 1 (aún no se ha prestado)");
        System.out.println("Estado prestada actual:");
        System.out.println(pelicula1.getPrestada());

        System.out.println("\n04. VERIFICAR ESTADO DE PELÍCULA 1 para PRESTAPELÍCULA (ya fue presetada)");
        videoclub.prestaPelicula("My friend and I","drama",cliente1); //se presta la película
        System.out.println("Estado prestada actual:");
        System.out.println(pelicula1.getPrestada());

//        VERIFICAR EL ESTADO DE PRESTADO DE PELÍCULA 1
        System.out.println("\n05. VERIFICAR ESTADO DE PELÍCULA 1 para DEVOLVERPELÍCULA (luego de ser devuelta)");
        videoclub.devolverPelicula("My friend and I","drama",cliente1); // se devuelve la película

        System.out.println("Estado prestada actual:");
        System.out.println(pelicula1.getPrestada());

        //    ELIMINAR UNA PELÍCULA
        System.out.println("\n06. ELIMINAR PELÍCULA DEL VIDEOCLUB");
        System.out.println("Para eliminar una película, primero se chequea que existe la película que ha devuelto Isabella, se revisan las películas del género -drama-");
        System.out.println("DRAMA:");
        videoclub.imprimirGenero("drama");

        System.out.println("\nSe procede a eliminar la película. Como resultado, al imprimir las películas no debería aparecer ninguna.");

        videoclub.eliminarPelicula("My friend and I", "drama"); // se elimina la película del videoclub

//        VERIFICAR QUE SE HAYA ELIMINADO LA PELIÍCULA INDICADA
        System.out.println("\n07. VERIFICAR QUE SE HAYA ELIMINADO LA PELÍCULA INDICADA");
        System.out.println("DRAMA:");
        videoclub.imprimirGenero("drama");

        System.out.println("La lista está vacía, se ha eliminado correctamente la película.");
    }
}
