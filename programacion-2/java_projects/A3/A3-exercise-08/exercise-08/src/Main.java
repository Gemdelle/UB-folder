// A3 EXERCISE 08
// La empresa “Never-NO” realiza transportes de diferentes tipos de carga, utilizando carreteras nacionales y provinciales. Para ello requiere vehículos especialmente acondicionados según la carga.

//Cada transporte se identifica por el número de patente y se mantiene la siguiente información:
//descripción de la carga
//localidad de salida
//localidad de llegada
//Las localidades están codificadas según el registro de códigos postales vigente.

//Datos adicionales según la carga a transportar:
// Alimentos: Lista de tipos de alimentos, cantidad a transportar de cada uno y su peso.

// Bultos: Cantidad de bultos de cada tamaño
// Bulto MINI: 0.01 a 20 kg.
// Bulto MID: 21 a 100 kg.
// Bulto MAX: 101 a 150 kg.
//Para el cálculo de peso se considera un promedio de dicho rango.

// Ganado: Cantidad de cabezas a transportar y peso promedio por cabeza

// Escribir un programa aplicando el concepto de polimorfismo que muestre el costo del viaje para un vehículo dado, sabiendo que éste depende no sólo del trayecto a realizar sino de la carga a transportar.
// Costo por peso transportado:
// Hasta 1200kg.: $ 6.00 por kg.
// Hasta 2400kg.: $ 5.50 por kg.
// Hasta 4000kg.: $ 4.30 por kg.
// Más de 4000kg.: $ 3.60 por kg.

// Los transportes se realizan entre 10 localidades. No siempre la tarifa de viajar de una localidad a otra es igual en caso de realizar el viaje inverso. Existe una matriz disponible de tarifas de transporte entre ciudades.

// Escribir un método (y mostrar su uso) que, para dos transportes A y B, indique aquél de mayor costo.
// Escribir un método en la clase aplicación que reciba un conjunto de transportes y muestre en pantalla su información según el tipo de transporte.

import java.util.ArrayList;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        ArrayList<Alimento> alimentos = crearAlimentosRandom();
        TransporteAlimentos transporteAlimentos = new TransporteAlimentos("AF 373 EQ", "Transporte de alimentos para la empresa Alimentos Copa2 S.A", "Buenos Aires", "Rosario", alimentos);
        System.out.printf("El transportador de Alimentos con patente [%s] pasó un costo total para transportar alimentos de: %f\n", transporteAlimentos.getPatente(), transporteAlimentos.calcularCostoTotal());

        TransporteBultos transporteBultos = new TransporteBultos("OK 666 KO", "Transporte mayorista de bultos de la empresa B's Veloces S.A", "Rosario", "Santa Fe", 70, 40, 6);
        System.out.printf("El transportador de Bultos con patente [OK 666 KO] pasó un costo total para transportar bultos de: %f\n", transporteBultos.calcularCostoTotal());

        TransporteGanado transporteGanado = new TransporteGanado("OL 123 LA", "Transporte de ganado para la empresa Mataderos del Sur S.A", "Misiones", "Cordoba", 35, 500);
        System.out.printf("El transportador de Ganado con patente [OL 123 LA] pasó un costo total para transportar el ganado de: %f\n", transporteGanado.calcularCostoTotal());
    }

    private static ArrayList<Alimento> crearAlimentosRandom() {
        Random random = new Random();
        ArrayList<Alimento> alimentos = new ArrayList<>();
        for (int i = 0; i < 20; i++) {
            alimentos.add(new Alimento(random.nextInt(30 - 5) + 5, random.nextInt(50 - 20) + 20));
        }
        return alimentos;
    }
}
