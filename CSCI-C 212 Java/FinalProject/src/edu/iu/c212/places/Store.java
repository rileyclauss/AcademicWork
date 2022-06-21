package edu.iu.c212.places;

import edu.iu.c212.Arcade;
import edu.iu.c212.models.Item;
import edu.iu.c212.models.User;
import edu.iu.c212.utils.ConsoleUtils;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Store extends Place{


    public Store(Arcade arcade){
        super.placeName = "Store";
        super.entryFee = 0;
        super.arcade = arcade;

    }

    @Override
    public void onEnter(User user) {
        List<String> options = new ArrayList<String>();
        options.add("Buy an item.");
        options.add("Sell an item.");
        options.add("Leave the store.");        //Allow the user to pick their intended action
        String chosen = ConsoleUtils.printMenuToConsole("Store menu: ",options, true);
        if (chosen.equals(options.get(0))){                 //If they want to Buy and item,
            if (user.getInventory().size() == 3){           //check if they already have three items
                System.out.println("You already have 3 items."); //if they do, tell the player
                arcade.transitionArcadeState("Lobby");          //and send them back to the lobby
            }
            options.clear();                        //otherwise, clear the options
            for (Item i : Item.values()){           //and repopulate it with each item available
                options.add(i.toString());
            }
            options.add("Exit");                    //or an exit option
            System.out.println("Your balance is currently $" + user.getBalance());
            chosen = ConsoleUtils.printMenuToConsole("Pick an item: ",options,true);
            if(chosen.equals(options.get(10))){     //if they pick exit, quit before doing anything else
                arcade.transitionArcadeState("Lobby");
            }
            else{       //otherwise, set the intended item from the corresponding option chosen
                Item i = Item.TRINKET;  //defaulting to Trinket because my compiler didn't like that i didn't have a default value
                if (chosen.equals(options.get(0))){
                    i = Item.TRINKET;
                }
                else if(chosen.equals(options.get(1))){
                    i = Item.NECKLACE;
                }
                else if(chosen.equals(options.get(2))){
                    i = Item.CANDY;
                }
                else if(chosen.equals(options.get(3))){
                    i = Item.VIDEOGAME;
                }
                else if(chosen.equals(options.get(4))){
                    i = Item.SANDWICH;
                }
                else if(chosen.equals(options.get(5))){
                    i = Item.RCCAR;
                }
                else if(chosen.equals(options.get(6))){
                    i = Item.TV;
                }
                else if(chosen.equals(options.get(7))){
                    i = Item.SODA;
                }
                else if(chosen.equals(options.get(8))){
                    i = Item.LAPTOP;
                }
                else if(chosen.equals(options.get(9))){
                    i = Item.THEARCADE;
                }
                else{   //if they somehow chose something else, send them back to the entrance of the store
                    System.out.println("It seems you didn't choose a valid option, please try again.");
                    arcade.transitionArcadeState("Store");
                }

                if (i.getValue() > user.getBalance()){  //if the item is too expensive, don't let the user purchase it
                    System.out.println("Item has value " + i.getValue() + ", but you only have " + user.getBalance());
                    arcade.transitionArcadeState("Store");
                }
                else{   //otherise check that the user is sure they want to purchase it
                    options.clear();
                    options.add("Y");
                    options.add("N");
                    chosen = ConsoleUtils.printMenuToConsole("Item has value " + i.getValue() + ", you have " + user.getBalance() + ".\nAre you sure you'd like to buy this?",options,true);
                    if (chosen.equals(options.get(0))){ //if they do, remove the value from their balance
                        user.setBalance(user.getBalance()-i.getValue());
                        user.addItem(i);        //and add it to their inventory
                        System.out.println("You successfully bought the item! You now have a balnce of " + user.getBalance());
                        try {       //then save these changes to their file
                            arcade.saveUsersToFile();
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    }
                    else{   //if they decide not to buy it, do nothing
                        System.out.println("You did not buy the item. Your balance remains " + user.getBalance());
                    }
                    arcade.transitionArcadeState("Store"); //either way, return the user to the store entrance
                }
            }
        }
        else if (chosen.equals(options.get(1))){        //if the user wants to sell something
            if (user.getInventory().size() < 1){        //make sure they have something to sell
                System.out.println("You do not have any items to sell.");
                arcade.transitionArcadeState("Lobby");  //if they don't, kick them back to the lobby
            }
            options.clear();
            for(Item i : user.getInventory()){
                options.add(i.toString());  //add each item from their inventory to the available options
            }
            chosen = ConsoleUtils.printMenuToConsole("Pick an item to sell for half its value: ", options, true);
            Item i = null;
            for (String s : options){
                if (s.equals(chosen)){
                    i = Item.findByKey(s.split("-")[0]);    //then pick the enum item they chose from the menu
                }
            }
            System.out.println("Selling this item will give you $"+(i.getValue()/2));   //Warn the user they will only get half the original value
            options.clear();
            options.add("Y");
            options.add("N");   //and make sure they still want to sell it
            chosen = ConsoleUtils.printMenuToConsole("Would you like to sell this item?", options, true);
            if (chosen.equals(options.get(0))){ //if they do, remove it from their inventory and update their balance
                user.removeItem(i);
                user.setBalance(user.getBalance()+(i.getValue()/2));
            }
            try {
                arcade.saveUsersToFile();
            } catch (IOException e) {
                e.printStackTrace();
            }
            arcade.transitionArcadeState("Store");  //either way, return them to the store entrance
        }
        else{
            arcade.transitionArcadeState("Lobby");
        }

    }

    enum StoreAction{
        BUY,SELL,LEAVE;
    }
}
