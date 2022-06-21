package edu.iu.c212.places;

import edu.iu.c212.Arcade;
import edu.iu.c212.models.Item;
import edu.iu.c212.models.User;

public class Inventory extends Place {

    public Inventory(Arcade arcade){
        super.placeName = "Inventory";
        super.entryFee = 0;
        super.arcade = arcade;
    }

    @Override
    public void onEnter(User user) {
        System.out.println("Hello, " + user.getUsername() +"! Your inventory looks like this: ");
        int amt = 0;                            //count how many items the user has,
        double worth = 0;                       //and the worth of their inventory
        for (Item i : user.getInventory()){     //For each item in their inventory
            worth+= i.getValue();               //add to the worth,
            System.out.println(i.toString());   //print the name and value,
            amt++;                              //and increment number of items
        }
        worth+= user.getBalance();              //finally add the user's balance to their worth
        System.out.println("You currently have $" + user.getBalance() + ", your net worth is $" + worth);
        if (amt == 3){      //if they have three items (the max number of items) display a warning
            System.out.println("Remember! You can only hold three items at once.");
        }
        //then return to the lobby
        arcade.transitionArcadeState("Lobby");
    }
}
