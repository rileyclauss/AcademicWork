package edu.iu.c212.places;

import edu.iu.c212.Arcade;
import edu.iu.c212.models.User;

public abstract class Place {

    protected String placeName;
    protected Arcade arcade;
    protected double entryFee;
    public abstract void onEnter(User user);
    @Override
    public String toString(){
        return this.placeName +", "+ this.entryFee + ", not a game.";
    }


}
