package edu.iu.c212.places.games.blackjack;

import java.util.Collections;

public class BlackjackDealer extends BlackjackParticipant {

    private char shownCard;     //Shown card is a single character, refer to BlackjackPlayer.java for possible values
    private int dealerBest;     //Dealer best is set during the dealer's turn and checked for victory at the end of the game
    
    public BlackjackDealer(){   
        this.shownCard = 'E';   //The dealer's shown card is set to E to start, which signals hit() to store the first card here
        super.handTotals = (new int[]{0,10}); //the first value is with an Ace as 1, the second is an ace as 11. This way, the second value will always be 10 more than the first
        Collections.shuffle(cards); //cards are shuffled
        hit(cards.remove(0));       //and dealt to the dealer
        Collections.shuffle(cards); 
        hit(cards.remove(0));
    }

    @Override
    public void hit(char c){
        if (c == 'A'){                  //if the card dealt was an Ace,
            this.hasAce = true;
            this.handTotals[0] += 1;    //add one to both values and set hasAce to true
            this.handTotals[1] += 1;    //which tells the other methods to use the second value as well if it's under 21
        }
        else if (c == 'T'){             //T represents 10 as a character
            this.handTotals[0] += 10;
            this.handTotals[1] += 10;
        }
        else{
            this.handTotals[0] += Integer.valueOf(c - '0'); //this extracts the true integer value from the card value character
            this.handTotals[1] += Integer.valueOf(c - '0');
        }
        if (shownCard == 'E'){          //this is called only for the dealer's first hit
            this.shownCard = c;
        }
        this.dealerBest = getBestTotal();   //reset the dealerBest value
    }

    public String getPartialHand(){         //this returns the string for the dealer's hand to the player
        if (shownCard == 'T'){
            return "[ 10 + ? ]";        //whose only special case is a T for 10
        }
        return "[ " + shownCard + " + ? ]";
    }

    public void play(){
        boolean hitMe = true;           //this method is called after the user busts or stays
        while(hitMe){
            if (getBestTotal() > 21){   //if the dealer busts, set dealerBest to -1 and quit the loop
                dealerBest = -1;
                hitMe = false;
            }
            else if(getBestTotal() > 16){       //if the dealer has 17 or more, that's his final value
                dealerBest = getBestTotal();
                hitMe = false;
            }
            else{
                Collections.shuffle(cards);     //otherwise shuffle and pull a card
                hit(cards.remove(0));
            }
        }

    }

    public int getDealerBest(){
        return this.dealerBest;
    }


    @Override
    public int getBestTotal() {
        if (this.hasAce && this.handTotals[1]<=21){     //if the dealer has an ace, and that would not bust him
            return this.handTotals[1];                  //return the second, higher value
        }
        else{
            return this.handTotals[0];
        }
    }
}
