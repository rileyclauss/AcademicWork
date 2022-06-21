import java.awt.*;
import java.awt.JButton;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;




public class BlackjackPlayer{


    private static int[] handTotals;
    private static int[] dealerTotals;
    private static boolean bust;
    private static boolean dealerAce;
    private static boolean playerAce;
    private static JLabel totalsLabel;
    private static JLabel dealerLabel;
    private static JButton hit;
    private static JButton stay;
    private static Deck playDeck;

    public BlackjackPlayer(){}

    public static void main(String[] args) {
        JFrame frame = new JFrame();
        JPanel mainPanel = new JPanel();  //total panel that will take status and buttons
        JPanel statusPanel = new JPanel();
        JPanel buttonsPanel = new JPanel();
        dealerLabel = new JLabel("dealer label");  //label that displays the dealer's hand
        statusPanel.add(dealerLabel);
        totalsLabel = new JLabel("total label");   //and label that displays the player's hand
        statusPanel.add(totalsLabel);
        hit = new JButton("Hit me!");              //buttons for gameplay
        stay = new JButton("Stay!");        
        hit.addActionListener(new HitButtonListener());     //add relevant listeners to each button
        stay.addActionListener(new StayButtonListener());
        buttonsPanel.add(hit);                              //and add those buttons to their panel
        buttonsPanel.add(stay);
        mainPanel.setSize(new Dimension (500,500));         
        statusPanel.setSize(new Dimension(500,300));
        buttonsPanel.setSize(new Dimension(500,200));
        mainPanel.add(statusPanel);                     //add the button and status panels to the main panel
        mainPanel.add(buttonsPanel);
        mainPanel.setBackground(Color.green);
        frame.getContentPane().add(mainPanel);          //and add the main panel to the frame
        frame.pack();
        frame.setSize(new Dimension(500,500));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        play();             //starts the game itself
    }

    public static void play(){
        handTotals = new int[2];        //handTotals is two values, one with ace as 1 and the other with ace as 11
        dealerTotals = new int[2];      //dealer is given additional capacity for functionality without that added functionality, just to keep things even and readable
        playDeck = new Deck();          //create a new Deck, a custom class with an arraylist of all values
        int newCard = playDeck.pullCard();  //pull a card from the deck, which returns the int value of the card
        addCard(newCard, 0);                //add the card to the player's hand, 0 being player and 1 being dealer as in line 64
        newCard = playDeck.pullCard();
        addCard(newCard, 0);                //pull and add another card
        newCard = playDeck.pullCard();
        addCard(newCard, 1);                //pull one last card for the dealer
        updateLabels();                     //and update the labels

    }
    public static void updateLabels(){
        if (dealerAce && dealerTotals[1] > 21) dealerAce = false;       //if dealer/player has an ace, and the ace as an 11 puts them over 21
        if (playerAce && handTotals[1] > 21) playerAce = false;         //then the ace is only equal to 1, in handTotals[0] or dealerTotals[0]
        dealerLabel.setText("Dealer has " +(dealerAce ? ""+dealerTotals[0]+"/"+dealerTotals[1]:dealerTotals[0])+" + ???");    //displays scores different based on if an ace is in their hand
        totalsLabel.setText("You have " + (playerAce?""+handTotals[0]+"/"+handTotals[1]:handTotals[0]));
    }

    public static void addCard(int val, int hand){

        if (hand == 0){                     //if hand == 0, the card goes to the player
            System.out.println("Player gets a" + (val == -1 ? "n ace" : " " + val));        //log what the player pulled
            if (val == -1){             //if it's -1, representing an ace,
                handTotals[0] += 1;     //add one to handTotals[0]
                handTotals[1] += 11;    //and 11 to handTotals[1]
                playerAce = true;
            }
            else{
                handTotals[0] += val;       //if it's not an ace, add the value
                handTotals[1] += val;       //to each version of the hand
            }
        }
        else{                               //otherwise the card goes to the dealer
            System.out.println("SECRET: Dealer gets a" + (val == -1 ? "n ace" : " " + val));
            if (val == -1){
                dealerTotals[0] += 1;       //same as above
                dealerTotals[1] += 11;
                dealerAce = true;
            }
            else{
                dealerTotals[0] += val;
                dealerTotals[1] += val;
            }
        }

    }




    private static class HitButtonListener implements ActionListener{
        public void actionPerformed(ActionEvent e){
            int newCard = playDeck.pullCard();      //Hit just pulls a new card
            addCard(newCard, 0);                    //and adds it to the deck,
            updateLabels();                         //and updates the labels
        }
    }
    private static class StayButtonListener implements ActionListener{
        public void actionPerformed(ActionEvent e){
            int dealerFinal = (dealerAce ? dealerTotals[1]:dealerTotals[0]);        //gather the final score of the dealer
            int playerFinal = (playerAce ? handTotals[1]:handTotals[0]);            //and the player
            totalsLabel.setText((playerFinal>dealerFinal)?"You win!":"You lose :(");    //if the player has a higher score over the dealer, they win
            if (playerFinal >21) totalsLabel.setText("You busted!");                    //unless they have over 21, in which case they bust
        }
    }
}