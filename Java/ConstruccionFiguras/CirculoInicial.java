package principal;

public class CirculoInicial {
    
    private int radio;
    public int getRadio(int radio){
        return radio;
    }
    public void setRadio(int radio){
        this.radio = radio;
    }
    public double calcularArea(int x, int y, int radio){
        return (Math.PI * Math.pow(radio, 2));
    
    }
}