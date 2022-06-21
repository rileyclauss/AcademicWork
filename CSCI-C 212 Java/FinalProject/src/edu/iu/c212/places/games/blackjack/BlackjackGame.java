package edu.iu.c212.places.games.blackjack;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import edu.iu.c212.Arcade;
import edu.iu.c212.models.User;
import edu.iu.c212.places.games.Game;
import edu.iu.c212.utils.ConsoleUtils;

public class BlackjackGame extends Game {


    public BlackjackGame(Arcade arcade){
        super.placeName = "Blackjack";
        super.entryFee = 20.0;
        super.arcade = arcade;
    }



    @Override
    public void onEnter(User user) {
        user.setBalance(user.getBalance()-this.entryFee);   //take the entry fee and save
        try {
            arcade.saveUsersToFile();
        } catch (IOException e1) {
            e1.printStackTrace();
        }
        System.out.println("Blackjack's back! If you win, you'll get $50! Remember, you want a total as close to 21 as possible without going over. If you bust (go over 21), or end with a lower or equal total to the dealer, you lose. Aces are either worth 1 or 11, whichever is better for your hand. Good luck!");
        BlackjackPlayer you = new BlackjackPlayer();            //This is the user
        BlackjackDealer dealer = new BlackjackDealer();         //and the dealer object
        List<String> options = new ArrayList<String>();
        options.add("Hit");
        options.add("Stay");
        String chosen;
        boolean playing = true;
        while(playing){
            if (you.getBestTotal() > 21){                     //Whether the user is over 21 or not is checked first
                System.out.println("You busted!");
                dealer.play();                              //it really doesn't matter if the dealer plays, the user has already lost
                playing = false;                            //and if so, they're kicked to the end of the game
                break;
            }
            chosen = ConsoleUtils.printMenuToConsole("Dealer's hand: " + dealer.getPartialHand() + "\nYour hand: " + you.getTotalsString(), options, true);
            if (chosen.equals(options.get(0))){         //otherwise, if the user chooses to hit
                Collections.shuffle(BlackjackPlayer.cards); //the cards are shuffled and one is dealed to them
                you.hit(BlackjackPlayer.cards.remove(0));
            }
            else{                           //otherwise, the dealer plays until they're done
                dealer.play();
                playing = false;            //and the game ends
            }

        }
        //if the user total is greater than the dealer, and the user has not busted,
        if (you.getBestTotal() > dealer.getDealerBest() && you.getBestTotal() <= 21){
            System.out.println("You win! You get $50! The dealer had " + dealer.getBestTotal() + " and you had " + you.getBestTotal());
            user.setBalance(user.getBalance()+50.0);    //the user wins $50
            try {
                arcade.saveUsersToFile();               //which is saved to the file
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        else{   //otherwise, the user's total is lower than the dealer or they busted, so they lose and win nothing
            System.out.println("Sorry, you lost. The dealer had " + dealer.getBestTotal() + " and you had " + you.getBestTotal());
        }
        //eiher way, the user is returned to the lobby
        System.out.println("Returning to the lobby...");
        arcade.transitionArcadeState("Lobby");
    }
}
