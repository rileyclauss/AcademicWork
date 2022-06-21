package edu.iu.c212.places.games.blackjack;

import java.util.ArrayList;

public abstract class BlackjackParticipant {

    protected static ArrayList<Character> cards;
    protected int[] handTotals;
    protected boolean hasAce;


    public void hit(char c){        //Basic hit method that notifies the user as they are pulling the card
        if (c == 'A'){
            System.out.println("You were dealt an ace.");
            hasAce = true;
            handTotals[0] += 1;
            handTotals[1] += 1;
        }
        else if (c == 'T'){
            System.out.println("You were dealt a ten/suit card.");
            handTotals[0] += 10;
            handTotals[1] += 10;
        }
        else{
            System.out.println("You were dealt a " + c + ".");
            handTotals[0] += Integer.valueOf(c - '0');
            handTotals[1] += Integer.valueOf(c - '0');
        }
    }

    public abstract int getBestTotal(); 

}
