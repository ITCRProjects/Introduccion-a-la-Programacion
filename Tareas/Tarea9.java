import java.util.Scanner;

public class Tarea9{

    public static void main(String[] args) {
        System.out.println("Introduzca los numeros que desea sumar, si introduce 0, termina: ");
        Scanner sc = new Scanner(System.in); //just copy-and paste this line, you dont have to understand it yet.
        int numero;
        int suma = 0;
        do {
            numero = sc.nextInt(); //this reads number from input and store its value in variable number
            suma+= numero; //here you add number to the total sum
        } while(numero != 0); //just repeat cycle as long as number is not zero

        System.out.println("El resultado de la suma de los números ingresados es el siguiente : " + suma);
    }

}