package principal;

public class FiguraInicial {
    private int x;
    private int y;
    
    public int getX(int x){
        return this.x;
    }
    public void setX(int x){
        if ((x >= 0) & (x <= 1023)){
            this.x = x;
        }
        else{
            System.out.println("El valor de x debe ser mayor o igual a 0 y menor a 1024");
        }
    }
    public int getY(int y){
        return this.y;
    }
    public void setY(int y){
        if ((y >= 0) & (x <= 768)){
            this.y = y;
        }
        else{
            System.out.println("El valor de y debe ser mayor o igual a 0 y menor a 769");
        }
    }
}