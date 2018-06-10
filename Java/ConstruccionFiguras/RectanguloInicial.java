
package principal;

public class RectanguloInicial {
    
    private int ancho;
    private int alto;
            
    public int getAlto(int alto){
        return alto;
    }
    public void setAlto(int alto){
        this.alto = alto;
    }
    public int getAncho(int ancho){
        return ancho;
    }
    public void setAncho(int ancho){
        this.ancho = ancho;
    }
    public double calcularArea(int x, int y, int ancho, int alto){
        return alto * ancho;
    }
    
}