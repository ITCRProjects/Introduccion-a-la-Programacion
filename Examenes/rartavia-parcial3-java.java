
import java.util.Scanner;

public class Parte1{

	public Parte1(){}

		int contador;
		int contador2;
		int i;

		public int contar(int numero){
			while (int numero/10 != 0){
				numero = numero/10;
				contador = contador + 1;}
			return contador;}

		public int[] ordenarLista(int[] lista){
			int[] vector = new int[lista.lenght];
			while (contador2 <= vector.lenght-1){
				for(i = 0,i < vector.lenght,i++){
					if vector[i] < vector[i+1]{
						vector[i] = vector[i+1];
						vector[i+1] = vector[i];}}}

				return vector;}
		
		public static void main(String[] args){
			Parte1 parte1 = new Parte1();
			System.out.println("Ingrese un número al que le desea contar sus digitos: ");
			Scanner entrada = new Scanner(System.in);
			int numero = entrada.nextInt();
			int cuenta = parte1.contar(numero);
			System.out.println("El número tiene la siguiente cantidad de digitos: " + cuenta);
			System.out.println("Ingrese la lista que desea ordenar: ");
			int[] listaIngresada = new Scanner(System.in);
			int ordenar = parte1.ordenarLista(listaIngresada);
			System.out.println("El resultado de ordenar la lista es: " + ordenar);}}

	















}