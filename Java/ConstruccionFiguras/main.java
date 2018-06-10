package principal;

import java.util.Scanner;

public class Main {
    
    public static void main(String[] args){
    
        CirculoInicial circ = new CirculoInicial();
        RectanguloInicial rect = new RectanguloInicial();
        
        
        System.out.println("*** Menú ***");
        System.out.println("1. Calcular Area para Circulo.");
        System.out.println("2. Calcular Area para Rectangulo.");
        System.out.println("Ingrese la opción que desea ejecutar.");
        
        
        Scanner entrada = new Scanner(System.in);
        int opcion = entrada.nextInt();
        System.out.println("Ingrese el Ancho de la pantalla: ");
        int valor1 = entrada.nextInt();
        System.out.println("Ingrese el Alto de la pantalla: ");
        int valor2 = entrada.nextInt();
       
       
        double resultado = 0;
        switch(opcion){
            case 1: 
                System.out.println("Ingrese el Radio del Circulo: ");
                int valor3 = entrada.nextInt();
                resultado = circ.calcularArea(valor1, valor2, valor3);
                break;
            case 2:
                System.out.println("Ingrese el Alto del Retangulo: ");
                int valor4 = entrada.nextInt();
                System.out.println("Ingrese el Ancho del Retangulo: ");
                int valor5 = entrada.nextInt();
                resultado = rect.calcularArea(valor1, valor2, valor4, valor5);
                break;
            default:
                System.out.println("Default case");
        }
        System.out.println("El Area correspondiente es: " + resultado);
    
    }
}