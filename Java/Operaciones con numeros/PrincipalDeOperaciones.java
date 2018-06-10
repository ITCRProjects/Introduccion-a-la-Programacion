package principal;
import clases.Operaciones;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args){
        
        int opcion = 0;   
        do{ 
            menu();
            Scanner entrada = new Scanner(System.in);
            opcion = entrada.nextInt();
            
            if (opcion != 5){
                proceso(opcion,entrada);
                
                }
            }   
            while (opcion >= 1 && opcion <= 4);
            System.out.println("Salió con Exito.");
        }
    
    public static void menu(){
        System.out.println("*** Menú ***");
        System.out.println("1. Suma.");
        System.out.println("2. Resta.");
        System.out.println("3. Multiplicación.");
        System.out.println("4. División.");
        System.out.println("5. Salir");
        System.out.println("Ingrese la opción que desea ejecutar.");
        }
    
    public static void proceso(int opcion, Scanner entrada){
        Operaciones oper = new Operaciones();
        System.out.println("Ingrese el Valor 1: ");
        int valor1 = entrada.nextInt();
        System.out.println("Ingrese el Valor 2: ");
        int valor2 = entrada.nextInt();
            
        double resultado = 0;
        
        switch(opcion){
                case 1: 
                    resultado = oper.suma(valor1, valor2);
                        break;
                case 2:
                    resultado = oper.resta(valor1, valor2);
                        break;
                case 3:
                    resultado = oper.multiplicacion(valor1, valor2);
                        break;
                case 4:
                    resultado = oper.division(valor1, valor2);
                    break;
                default:
                    System.out.println("No se realizó ninguna operación.");
                }
                System.out.println("El resultado es: " + resultado);
    }
    
}