package edu.iu.c212.models;

import java.util.ArrayList;
import java.util.List;


public class User {

    private String username;
    private double balance;
    private List<Item> inventory;
    /*
    This class is just for each user, it contains their name, balance, and inventory.
    There's only basic getters and setters here, as well as addItem and removeItem
    for buying and selling in the shop.
    */


    public User(String username, double balance){
        this.username = username;
        this.balance = balance;
        this.inventory = new ArrayList<Item>();
    }
    public void setUsername(String username){
        this.username = username;
    }
    public String getUsername(){
        return this.username;
    }
    public void setBalance(double balance){
        this.balance = balance;
    }
    public double getBalance(){
        return this.balance;
    }
    public void setInventory(List<Item> inventory){
        this.inventory = inventory;
    }
    public List<Item> getInventory(){
        return this.inventory;
    }
    public void addItem(Item item){
        this.inventory.add(item);
    }
    public void removeItem(Item item){
        this.inventory.remove(item);
    }



}
