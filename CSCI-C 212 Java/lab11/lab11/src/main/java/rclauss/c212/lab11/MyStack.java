package rclauss.c212.lab11;
import java.util.*;

public class MyStack {      //naming the file Stack.java created some issue with the util.Stack import

    public static void main(String[] args) {
        System.out.println("1234321:\nExpected: true -- Actual: "+isIntPalindrome(1234321));
        System.out.println("1234567:\nExpected: false -- Actual: "+isIntPalindrome(1234567));
        System.out.println("'rAcEcaR':\nExpected: true -- Actual: "+ isStrPalindrome("rAcEcaR"));
        System.out.println("'palindrome':\nExpected: false -- Actual: "+isStrPalindrome("palindrome"));
    }


    public static Boolean isIntPalindrome(int num){
        int comp = 0, input = num, magnitude = 1; //comp is the int we will compare with, input is to preserve the original number
        //  as it will be modified, and magnitude helps place the numbers in the right order for comparison

        Stack<Integer> st = new Stack<Integer>();
        while(num > 0){     //while the number is greater than 0,
            st.push(num % 10);      //take the least significant digit
            num /= 10;              //then remove it
        }
        while(!st.empty()){
            comp += st.pop() * magnitude;       //add the most significant digit to the Xs place, beginning with 1
            magnitude *= 10;                    //then increment magnitude by 10
            //this puts the least significant digit form the input into the most significant digit in the comparison
        }
        return comp == input;

    }

    public static Boolean isStrPalindrome(String str){

        str = str.toLowerCase();        //convert the whole thing to lowercase first
        if (str.length() % 2 == 1){     //if the string is of odd length, remove the middle character as it does not matter
            str = str.substring(0, str.length()/2) + str.substring((str.length()/2) + 1);
        }
        int len = str.length()/2, i = 0;
        Stack<Character> st = new Stack<Character>();
        for (i = 0; i<len;i++){     //from the first character to the half of the string
            st.push(str.charAt(0));     //take the first char
            str = str.substring(1);     //and remove it from the string
        }
        while(!st.empty()){
            char x = st.pop();          //take the last-added character from the stack
            if (x != str.charAt(0)){    //compare it to its corresponding original character
                return false;           //if it's different, return false
            }
            str = str.substring(1);     //otherwise, continue chopping the string forward until the stack is empty
        }
        return true;                    //if the stack is emptied and each character is equal, then it is a palindrome.
    }


}