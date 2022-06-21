package edu.iu.c212.places;

import edu.iu.c212.Arcade;
import edu.iu.c212.models.User;
import edu.iu.c212.utils.ConsoleUtils;

import java.util.ArrayList;
import java.util.List;

public class Lobby extends Place{

    public Lobby(Arcade arcade){
        super.placeName = "Lobby";
        super.entryFee = 0;
        super.arcade = arcade;

    }

    @Override
    public void onEnter(User user) {
        List<String> options = new ArrayList<String>();
        for (Place p : arcade.getAllPlaces()){      //get each place into the list of options
            options.add(p.toString());
        }
        options.add("Exit the arcade.");        //and add an extra for quitting execution
        String goTo = ConsoleUtils.printMenuToConsole("Welcome to the arcade "+this.placeName+", "+user.getUsername(),options,true);
        arcade.transitionArcadeState(goTo);     //then get where the user would like to go and give it to the arcade transition method
    }
}
