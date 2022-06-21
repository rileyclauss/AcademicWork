package rclauss.c212.lab5;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;



public final class MinMaxStrings {
    public static boolean RUNEX1 = false;
    private MinMaxStrings() {
    }

    /**
     * Says hello to the world.
     * @param args The arguments of the program.
     */
    public static void main(String[] args) {
        if (RUNEX1){
            System.out.println("Enter a series of strings 1 by 1, then input -1 to quit.");
            ArrayList<String> strs = new ArrayList<String>();
            Scanner cin = new Scanner(System.in);
            boolean done = false;
            String input = "";
            while (!done){
                
                input = cin.nextLine();
                if (input.equals("-1")){
                    cin.close();
                    done = true;
                }
                else
                    strs.add(input);
                
            }
            System.out.println(strs.size()); 
            minMaxStr(strs);
        }
        


    }

    public static void minMaxStr(ArrayList<String> strs){
    
        int[] minMax = {strs.get(0).length(),0};
        String[] minMaxStr = new String[2];
        ArrayList<Integer> lens = new ArrayList<Integer>();
        System.out.println("Strings: " + strs.toString().replace("[", "{ ").replace("]", " }"));
        System.out.print("Length of Strings: { ");
        for (int i = 0;i<strs.size();i++){
            lens.add(strs.get(i).length());
            if (i != strs.size()-1)
                System.out.print(lens.get(i) + ", ");
            else 
                System.out.print(lens.get(i) + " }\n");
            if (lens.get(i) > minMax[1]){
                minMax[1] = lens.get(i);
                minMaxStr[1] = strs.get(i);
            }
            if (lens.get(i) < minMax[0]){
                minMax[0] = lens.get(i);
                minMaxStr[0] = strs.get(i);
            }
        }
        System.out.println("Minimum and maximum length: " + Arrays.toString(minMax));
        System.out.println("Corresponding Strings: " + Arrays.toString(minMaxStr));
        
    }
}

