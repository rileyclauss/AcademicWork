package rclauss.c212.lab5;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Random;

public final class LargeTriangles{
    public LargeTriangles(){

    }

    public static void main(String[] args){
        
        ArrayList<MyTriangle> triangles = testTriangles();
        Scanner cin = new Scanner(System.in);
        System.out.println("Enter the threshold value: ");
        double thresh = cin.nextDouble();
        ArrayList<MyTriangle> lrgTri = findTriangles(triangles, thresh);
        if (lrgTri.size() > 0){
            for (int i = 0;i<lrgTri.size();i++){
                System.out.println("Triangle " + (i+1) + " area: " + lrgTri.get(i).getArea() + " base: " + lrgTri.get(i).base + ", height: " + lrgTri.get(i).height);
            }
        }
        else{
            System.out.println("No entered triangle has an area larger than the threshold.");
        }
        
    }




    public static ArrayList<MyTriangle> findTriangles(ArrayList<MyTriangle> list, double thresh){
        ArrayList<MyTriangle> lrgTri = new ArrayList<MyTriangle>();
        for (int i = 0;i<list.size();i++){
            if (list.get(i).getArea() >= thresh){
                lrgTri.add(list.get(i));
            }
        }
        return lrgTri;
    }

    public static ArrayList<MyTriangle> testTriangles(){
        ArrayList<MyTriangle> triangles = new ArrayList<MyTriangle>();
        Scanner cin = new Scanner(System.in);
        double base, height;
        for(int i = 0; i<10;i++){
            System.out.println("Enter a base value: ");
            base = cin.nextDouble();
            System.out.println("Enter a height value: ");
            height = cin.nextDouble();
            MyTriangle x = new MyTriangle(base, height);
            triangles.add(x);
        }
        return triangles;
    }

    public static ArrayList<MyTriangle> randomTriangles(){
        ArrayList<MyTriangle> triangles = new ArrayList<MyTriangle>();
        Random rng = new Random();
        for(int i = 0; i<10;i++){
            MyTriangle x = new MyTriangle(rng.nextDouble()*25,rng.nextDouble()*25);
            triangles.add(x);
        }
        return triangles;


    }
}