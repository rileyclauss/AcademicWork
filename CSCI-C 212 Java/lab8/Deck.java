import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class Deck{

    private ArrayList<Integer> values; //an array of values of each card
    private int cards = 52;             //and the number of cards left

    public Deck(){

    }

    public int pullCard(){
        values = new ArrayList<Integer>(Arrays.asList(1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-1,-1,-1,-1));
        Random rand = new Random();     //there are four sets of four tens, as 10, J, Q, and K all represent 10, and -1 represents the four aces
        int val = rand.nextInt(cards--);    //take a random value and decrement cards, as one is being pulled
        int ret = values.get(val);      //take the value of the card,
        values.remove(val);             //remove it from the deck
        return ret;                     //and deal (return) it to the player
    }

}