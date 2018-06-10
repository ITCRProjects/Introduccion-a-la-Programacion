import java.util.Scanner;

class Tarea8{


    public static int  busquedaBinaria(int valor,int[] lista){

        int bajo = 0;
        int alto = lista.length;
        int central =  ((bajo + alto) / 2);

        while(lista[central] != valor){

            if (valor < lista[central]){
                alto = central - 1;}
            else{
                bajo = central + 1;
                central = ((bajo + alto) / 2); }}

        return central;
    }

    public static void main(String []args){

        int[] lista = {1,2,3,4,5};
        Scanner sc = new Scanner(System.in);
        int valor = sc.nextInt();
        System.out.println("Iniciando en 0, el valor indicado está en la posición: " + busquedaBinaria(valor,lista));}}