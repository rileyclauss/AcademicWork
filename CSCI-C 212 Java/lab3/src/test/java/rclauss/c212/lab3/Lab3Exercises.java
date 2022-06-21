package rclauss.c212.lab3;
import java.io.CharArrayReader;
import java.util.Random;
import java.util.Scanner;

public final class Lab3Exercises {

    public static String pigLatinEncoder(String engInput) {
        final String consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ";
        final String vowels = "aeiouyAEIOUY";
        engInput = engInput + "-";
        if (vowels.contains(Character.toString(engInput.charAt(0)))) {
            engInput = engInput + "way";
        } else {
            boolean isY = false;
            for (int i = 0; i < engInput.length(); i++) {
                if ((engInput.substring(engInput.indexOf("-") + 1) != "")
                        & "yY".contains(Character.toString(engInput.charAt(0)))) {
                    isY = true;
                } else {
                    isY = false;
                }
                if (consonants.contains(Character.toString(engInput.charAt(0)))) {
                    engInput = engInput + engInput.charAt(0);
                    engInput = engInput.substring(1);
                    continue;
                } else if (vowels.contains(Character.toString(engInput.charAt(0))) || isY == true) {
                    engInput = engInput + "ay";
                    return engInput;
                } else {
                    engInput = engInput + engInput.charAt(0);
                    engInput = engInput.substring(0);
                    continue;
                }
            }
        }

        return engInput;

    }

    public static String pigLatinDecoder(String cText){

        //catch ambiguous case (last 4 characters are -way)
        //remove last two characters, put end back on front one by one
        if (cText.contains("-way")){
            cText = cText.substring(0, cText.length()-4);
            String mText = "(" + cText + "/w" + cText + ")";
            return mText;
        }
        else{
            String endT = cText.substring(cText.indexOf("-")+1);
            endT = endT.substring(0, endT.length()-2);
            cText = cText.substring(0, cText.indexOf("-"));
            for (int i = endT.length()-1;i>=0;i--){
                cText = endT.charAt(i) + cText;
            }
        }

        return cText;
    }



    public static String randomCarsGenerator(int numCars){
        String result = "";
        String[] colors = {"White", "Orange", "Blue", "Yellow","Police", "News" };
        String[] cars = {"Jeep", "Van", "Tesla", "Truck"};
        Random rand = new Random();
        for (int i = 0; i<numCars; i++){
            result += (colors[rand.nextInt(6)] + " " + cars[rand.nextInt(4)] + ", ");
        }
        return result.substring(0, result.length()-2);
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Insert a number to cars: ");
        String input = s.nextLine();
        String result = "";
        String cResult = "";
        if (input.contains(" ")) {
            String[] multiInput = input.split(" ");
            for (int i = 0; i < multiInput.length; i++) {
                result += pigLatinEncoder(multiInput[i]) + " ";
            }
        } else {
            result = pigLatinEncoder(input);
        }
        System.out.println(result);
        if (result.contains(" ")) {
            String[] multiInput = result.split(" ");
            for (int i = 0; i < multiInput.length; i++) {
                cResult += pigLatinDecoder(multiInput[i]) + " ";
            }
        } else {
            cResult = pigLatinDecoder(result);
        }
        System.out.println(cResult);
        int x = s.nextInt();
        System.out.println(randomCarsGenerator(x));
    }

}