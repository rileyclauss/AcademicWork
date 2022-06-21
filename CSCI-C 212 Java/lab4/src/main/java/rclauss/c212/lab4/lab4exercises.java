package rclauss.c212.lab4;

import java.util.Random;
import java.util.Scanner;


public final class lab4exercises {

    public static void main(String[] args) {
        // secretNumber();
        // exponentCalculator(4, 7); // 16384
        // designingPatterns();
        // myMethod(3, 4);
        // gradeRileysLab4('A+');
    }

    public static void secretNumber() {
        Random rng = new Random();  //create the number generator
        int secretInt = rng.nextInt(10) + 1; //ceiling of 10(9), floor 0, add 1 to make range 1-10 inclusive 
        int guesses = 1; //number of guess, first guess is taken no matter what so default to 1
        int guess = 0; //first guess
        Scanner cin = new Scanner(System.in); 
        System.out.println("Guess a number between 1 and 10 inclusive: ");
        do { //first guess needs to be taken no matter what, so start without evaluation condition
            guess = cin.nextInt(); //take in guess
            if (guess < secretInt) { //if it's too low, print below
                System.out.println("Your guess was too low. Try again: ");
                guesses++;
            } else if (guess > secretInt) { //if it's too high, print below
                System.out.println("Your guess was too high. Try again: ");
                guesses++;
            }

        } while (guess != secretInt); // if/else statements don't assess ==, done here to exit loop
        System.out.println("Number guessed in " + guesses + " attempts."); //display success and number of guesses

    }

    public static int exponentCalculator(int base, int exponent) {
        int result = base;  //separate var for return var
        if (exponent < 0) { //if exponent is negative, exit computation
            System.out.println("Error. Exponent cannot be negative.");
            return -1; 
        } else if (exponent == 0) { //if exponent is 0, return 1
            return 1;
        } else if (base == 0) { //if base is 0, return 0
            return 0;
        }
        for (int i = 1; i < exponent; i++) { //exponential operation
            result *= base;
        }
        return result;
    }

    public static void designingPatterns() {
        Random rng = new Random(); //random number generator for size
        int size = rng.nextInt(8) + 3; 
        Scanner cin = new Scanner(System.in);
        boolean running = true; //if E has not been entered:
        System.out.println("Please select a pattern to display of size " + size);
        while (running) { // running is set to false when 'E' is entered
            System.out.println("A. Pattern 1\nB. Pattern 2\nC. Pattern 3\nD. Pattern 4\nR. Reroll Size\nE. Exit");
            switch (cin.nextLine().charAt(0)) { //If multiple characters are entered, just take the first
                case 'A':                                  //first pattern
                    for (int i = size - 1; i > 0; i--) {   //number of lines
                        System.out.print(" ");              
                        for (int j = 1; j < i; j++) {      // number of spaces conditional to line
                            System.out.print(" ");
                        }
                        for (int k = size; k > i; k--) {   // inverse of above with *s
                            System.out.print("*");
                        }
                        System.out.println();              // new line after line is written
                    }
                    for (int i = 1; i <= size; i++) {      // print opposite end of the pattern
                        for (int j = 1; j < i; j++) {      // same as above, just decreasing
                            System.out.print(" ");
                        }
                        for (int k = size; k >= i; k--) {
                            System.out.print("*");
                        }
                        System.out.println();
                    }
                    break;
                case 'B':      //second pattern
                    for (int i = 1; i <= size; i++) {  //number of lines
                        for (int j = 0; j < i; j++) {  // number of characters, same as line number
                            System.out.print(String.format("%d ", size));   //print size as num
                        }
                        System.out.println("");
                    }
                    break;
                case 'C':
                    String topAndBottom = "";                  //will become the top and bottom line
                    String middle = "";                        //will become the middle lines with proper num of spaces
                    for (int a = 2; a < size; a++) {           //generate top and bottom patterns, number of * = size - 2
                        topAndBottom += "* ";                  //sides will always need to be printer so topandbottom and middle
                        middle += "  ";                        //just need to fill the inbetween
                    }
                    for (int i = 1; i <= size; i++) {
                        System.out.print("* ");                //side will always be printed
                        if (i % size == 0 || size % i == 0) {  //if it's the first or last line
                            System.out.print(topAndBottom);    //print the top/bottom
                        } else {
                            System.out.print(middle);          //else print the spaces
                        }
                        System.out.print("*");                 //end of the side
                        System.out.println("");
                    }
                    break;
                case 'D': // checkerboard
                    for (int i = 1; i <= size; i++) {
                        for (int j = 1; j <= size; j++) {
                            int xor = (i + j) % 2;            //prints every other 'space' according to row
                            if (xor == 1) {                   //to make a checkerboard pattern
                                System.out.print("X");
                            } else {
                                System.out.print(" ");
                            }
                        }
                        System.out.println("");
                    }
                    break;
                case 'E':
                    running = false;                         //if E is entered, break
                    break;
                case 'R':
                    size = rng.nextInt(8) + 3;               //just for testing, resize the patterns
                    System.out.println("Size is now " + size);
                default:                                     //if something other than A, B, C, D, E, or R is entered, print error 
                    System.out.println("Invalid input, please enter A, B, C, D, R, or E: ");  //and return to top of loop
                    break;
            }
        }
    }

    public static void myMethod(int width, int height) {
        for (int i = 1; i <= height; i++) {            //number of rows
            for (int j = 1; j <= width; j++) {          //number of columns
                System.out.print("#");
            }
            System.out.println("");
        }
    }
}
