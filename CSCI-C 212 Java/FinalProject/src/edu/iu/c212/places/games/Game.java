package edu.iu.c212.places.games;

import edu.iu.c212.models.User;
import edu.iu.c212.places.Place;

public abstract class Game extends Place {

    @Override
    public String toString(){ 
        return this.placeName +", "+ this.entryFee + ", is a game.";
    }
}
