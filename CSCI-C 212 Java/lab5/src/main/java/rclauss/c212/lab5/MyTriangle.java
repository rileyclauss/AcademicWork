package rclauss.c212.lab5;

public final class MyTriangle{
    double base;
    double height;
    public MyTriangle(double b, double h){
        base = b;
        height = h;
    }
    public double getArea(){
        return (0.5 * base * height);
    }
}