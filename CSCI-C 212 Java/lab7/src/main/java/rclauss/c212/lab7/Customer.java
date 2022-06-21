package rclauss.c212.lab7;

import java.util.ArrayList;

public class Customer{

    private String customerName;      //basic attributes for Customer
    private ArrayList<Item> cart;     //customer gets their cart of Items
    private double budget;            //and a persistent budget
    private boolean wearingMask;      //if they are wearing a mask
    private ArrayList<Receipt> receipts; //and their previous transactions



    public Customer(String customerName, double budget, boolean wearingMask){
        this.customerName = customerName;
        this.budget = budget;
        this.wearingMask = wearingMask;
        this.cart = new ArrayList<Item>();
        this.receipts = new ArrayList<Receipt>();
    }

    public void addToCart(Item item){ //adding an item to their cart in the RetailStore customerMenu() method
        boolean multiple = false;     //used to see if the item is already in the cart
        for (Item i : cart){                               //for every item i already in the cart,
            if (i.getName().equals(item.getName())){       //if the given Item item is the same,
                multiple = true;                           //set multiple to true and increment the quantity of i in the cart
                i.setQuantity(i.getQuantity()+1);
            }
        }
        if (multiple == false){                            //if the item is not a multiple, add it to the cart with quantity 1
            cart.add(new Item(item.getName(), item.getPrice(), 1));
        }
    }

    public void addReceipt(Receipt receipt){
        this.receipts.add(receipt);                     //add a receipt to the customer's stack
    }
    public String getReceipts(){             //returns a string representation of the receipts
        String retS = "";
        for (Receipt r : this.receipts){
            retS += "" + r.getBreakdown() + "\r\n";
        }
        return retS;
    }

    public String getCustomerName() {
        return this.customerName;
    }


    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public ArrayList<Item> getCart() {
        return this.cart;
    }

    public double getBudget() {
        return this.budget;
    }

    public void setBudget(double budget) {
        this.budget = budget;
    }

    public boolean isWearingMask() {
        return this.wearingMask;
    }

    public void setWearingMask(boolean wearingMask) {
        this.wearingMask = wearingMask;
    }
}
