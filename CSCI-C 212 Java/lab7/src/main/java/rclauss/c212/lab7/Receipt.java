package rclauss.c212.lab7;

import java.util.ArrayList;

public class Receipt{
    private ArrayList<Item> items;

    public Receipt(ArrayList<Item> cart){
        this.items = cart;      //very simple class, just stores the manifest of a transaction
    }

    public String getBreakdown(){
        String retS = "";                 //and returns a string representation of it.
        double sum = 0;
        for (Item i : items){
            retS += "" + i.getQuantity() + "x " + i.getName() + " @$" + i.getPrice() + ":: ";
            sum += i.getQuantity() * i.getPrice();
        }
        return retS.subSequence(0, retS.length()-3) + ", Total: " + sum;
    }
}
