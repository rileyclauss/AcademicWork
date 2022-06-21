package rclauss.c212.lab7;

import java.util.ArrayList;
import java.util.Scanner;

public class RetailStore{

    private String name;           //Each store has a name, a list of products, and some customers
    private ArrayList<Item> items;          //I chose to use Items to store quantity of products rather than parallel arrays.
    private ArrayList<Customer> customers;
    private final double SALES_TAX = 0; //optional sales tax variable?

    public RetailStore(String name){
        this.name = name.isEmpty() ? "Dan Flash's" : name;   //A store needs a name to function properly, even if it's a duplicate
        this.items = new ArrayList<Item>();                 //Initialize the item and customer arrays
        this.customers = new ArrayList<Customer>();
    }

    public void addItem(String name, double price, int quantity){  //Adding an item to the store
        this.items.add(new Item(name,price,quantity));              //Item is created here rather than in RetailDriver
    }                                                               //but I did the opposite with customer since RetailDriver needs customer for
    public void addCustomer(Customer shopper){                      //the master list
        if (roomForCustomer() && shopper.isWearingMask()){      //If there's room for the customer and they're wearing a mask
            customers.add(shopper);                             //Add them to the store
            Scanner cin = new Scanner(System.in);
            String input = "";
            System.out.println("Would you like to go shopping as this customer? (Y/N)");  //If the user would like to shop with this customer
            input = cin.nextLine();         //if this choice was not given it would be impossible to fill the stores beyond 5 shoppers
            if (input.equals("Y")){         //if the user would like to 'shop' with this customer, open the customer menu
                customerMenu(shopper);
            }
            else{
                return;
            }
        }
        else System.out.println(!roomForCustomer() ? "Cannot add another customer, store is at capacity." : "Customer must be wearing a mask.");
    }
    public void addCustomerDummy(Customer shopper){ //used to quickly add customers for the dummy data
        customers.add(shopper);
    }
    public String getName(){
        return this.name;
    }

    public boolean roomForCustomer(){ //test if there are already 5 people in the shop
        return customers.size() < 5;
    }

    private void displayItems(){ //display the name, price, and quantity of each item
        for (int i = 0; i < items.size();i++){
            System.out.println("("+(i+1)+") " + items.get(i).getName() + ": $" +items.get(i).getPrice() + ", " + items.get(i).getQuantity());
        }
    }
    public String getItems(){ //return a string of every item to display
        String retS = "";
        for (Item i : items){
            retS += i.getName() + ": $" +i.getPrice() + ", " + i.getQuantity() + "x\r\n";
        }
        return retS;
    }
    public String getCustomers(){ //same as getItems() but for customers
        String retS = "";
        for (Customer c : customers){
            retS += c.getCustomerName() + ", ";
        }
        return retS;
    }

    public void customerMenu(Customer shopper){
        System.out.println("Welcome to " + this.name + ", " + shopper.getCustomerName() + "!\r\nEnter the number of the item" +
        " you would like to add to your cart, or enter \"0\" to checkout.");
        Scanner cin = new Scanner(System.in);
        int input = -1;
        displayItems(); //Display every item available to the customer
        input = cin.nextInt(); // the user makes a selection of 1,2,3... for each item, or 0 to checkout
        cin.nextLine(); //eat newline characters
        while (input != 0){ //while the customer doesn't want to checkout,
            System.out.println(items.get(input-1).getName() + " added to cart.");
            shopper.addToCart(items.get(input-1));  //add selected item to cart. input -  1 is because the items are displayed starting with 1, but ArrayLists are 0 indexed
            items.get(input-1).setQuantity(items.get(input-1).getQuantity()-1); //reduce the quantity of the selected item by 1
            displayItems(); //display the new quantity of each item
            input = cin.nextInt(); // take a new input
            cin.nextLine();
        }
        displayItems(); //display the final shelf
        double sum = 0;
        System.out.println("------------------------------------");
        System.out.println("Your cart contains: ");
        for (Item k : shopper.getCart()){ //for each item in the shelf,
            System.out.println("" + k.getQuantity()+"x " + k.getName() +" @$" + k.getPrice()); //display the name, amount, and price
            sum += k.getPrice() * k.getQuantity(); //and sum the total cost
        }
        sum += (sum*SALES_TAX);
        System.out.println("Your budget is $" + shopper.getBudget());  //show how much the customer can spend
        System.out.println("Your total is $" + sum);
        System.out.println("Would you like to check out? (Y/N)?");
        String inputS = cin.nextLine();
        if (inputS.equals("Y")){
            if (shopper.getBudget() > sum){ //Check that the customer has enough money
                shopper.setBudget(shopper.getBudget() - sum); //set their budget minus their total
                shopper.addReceipt(new Receipt(shopper.getCart())); //add a receipt to the customer's "stack"
                customers.remove(customers.indexOf(shopper)); //and remove them from the store, representing them exiting
            }
            else{
                System.out.println("You do not have enough money for this purchase."); //if the customer does not have enough in their budget,
                for (Item i : shopper.getCart()){
                    for (Item j : items){
                        if (i.getName().equals(j.getName())){ //put their cart back on shelves
                            j.setQuantity(j.getQuantity()+i.getQuantity());
                        }
                    }
                }
            }
        }
        else{                                            //or do the same if they answer anything other than "Y"
            for (Item i : shopper.getCart()){
                for (Item j : items){
                    if (i.getName().equals(j.getName())){
                        j.setQuantity(j.getQuantity()+i.getQuantity());
                    }
                }
            }
        }
    }

}
