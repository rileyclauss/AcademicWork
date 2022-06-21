package edu.iu.c212.models;

import java.util.HashMap;
import java.util.Map;

public enum Item {

    TRINKET  ("Trinket", 10),
    NECKLACE ("Necklace", 15),
    CANDY    ("Candy", 5),
    VIDEOGAME("VideoGame", 30),
    SANDWICH("Sandwich", 25),
    RCCAR("RCCar", 100),
    TV("TV", 200),
    SODA("Soda", 20),
    LAPTOP("Laptop", 500),
    THEARCADE("TheArcade", 10000);


    private final double value;
    private final String readableName;

    Item(String readableName, double value){
        this.readableName = readableName;
        this.value = value;
    }
    private static final Map<String,Item> map;      //this hashmap is solely for recognizing items from their name
    static{                                         //which mostly only happens when loading from the file to make sure
        map = new HashMap<String,Item>();           //each user's inventory persists between sessions
        for (Item i : Item.values()){
            map.put(i.readableName, i);
        }
    }
    public static Item findByKey(String name){      //so calling this with "Soda" would return the SODA item to add to the user's inventory
        return map.get(name);
    }

    @Override
    public String toString(){
        return "" + this.readableName + "-"+this.value;
    }

    public double getValue(){
        return this.value;
    }
}
