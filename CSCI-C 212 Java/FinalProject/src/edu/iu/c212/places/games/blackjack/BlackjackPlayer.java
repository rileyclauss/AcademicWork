package edu.iu.c212.places.games.blackjack;

import java.util.ArrayList;
import java.util.Collections;

public class BlackjackPlayer extends BlackjackParticipant{

    /*
    The rubric lists the extra credit as "allow for more than 2 handTotals," but there is no winning combination
    outside of two hand totals - regardless of how many aces a player has, only one can be worth 11. If
    I am dealt four aces, only one is worth 11, otherwise I bust. handTotals[0] counts any aces as one, and 
    handTotals[1] counts one ace as 11 and any additional as one, which are the only valid combinations.
    */


    public BlackjackPlayer(){
        super.handTotals = new int[2];
        super.cards = new ArrayList<Character>();   //the cards are initialized for the game here
        char addCard;
        for (int i = 1;i<=13;i++){  //there are 13 different 'numbers' including the suits 
            if(i == 1){             //Aces,
                addCard = 'A';
            }
            else if(i>=10){         //10s, Jacks, Queens, and Kings, all of which are 10s
                addCard = 'T';
            }
            else{                   //or 2 - 9, which are worth their normal value
                addCard = (char)(i+'0');
            }
            for (int j = 0; j<4;j++)     //There are four of each card, so 4 are added to the deck
                super.cards.add(addCard);
        }
        super.handTotals = (new int[]{0,10});   //as with the dealer, the user gets an aces-as-one hand and ace-as-11 hand
        Collections.shuffle(cards);             //Cards are shuffled and dealt like normal
        hit(cards.remove(0));
        Collections.shuffle(cards);
        hit(cards.remove(0));
    }

    public String getTotalsString(){
        if (this.hasAce && handTotals[1]<=21){  //If there's an ace and it's a valid hand, return both values
            return "[ " + handTotals[0] + ", " + handTotals[1] + " ]";
        }
        else{           //otherwise only the first value is needed
            return "[ " + handTotals[0] + " ]";
        }
    }

    @Override
    public int getBestTotal() {         //used for the final calculation
        if (this.hasAce && handTotals[1]<=21){
            return handTotals[1];           //if the user has an ace and it's under 21, return that value
        }
        else{
            return handTotals[0];           //otherwise return the normal/ace-as-one value
        }

    }

}
