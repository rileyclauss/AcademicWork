package rclauss.c212.lab7;

import java.util.Scanner;
import java.util.ArrayList;

public final class RetailDriver {

    private static ArrayList<Customer> customers = new ArrayList<Customer>(); //Array list for the storing of customers
    private static ArrayList<RetailStore> stores = new ArrayList<RetailStore>();  //And stores
    private static Scanner cin = new Scanner(System.in);  // I need a scanner in a few different methods so I declared it in this scope



    public static void displayMenu(){
        System.out.println("Would you like to (1) create a customer? (2) create a store? (3) create an item? (4) quit the program? (5) fill with dummy data? (6) print all data?");
        String input = cin.nextLine();  //Display a menu asking what the user would like to do,
        while (!input.equals("4")){  //With 4 being the quit program option
            switch(input){
                case "1":                           // 1 allows creation of a new customer,
                    createCustomer();
                    break;
                case "2":
                    createStore();             // 2 is for creating a new store
                    break;
                case "3":
                    createItem();               // 3 is for a new item
                    break;
                case "5":                  // 5 fills the program with premade data for ease of testing and demonstration
                    dummyData();
                    break;
                case "6":
                    printAll();           // 6 is also for testing/demonstration, printing off every customer and store
                    break;
            }
            System.out.println("Would you like to (1) create a customer? (2) create a store? (3) create an item? (4) quit the program? (5) fill with dummy data? (6) print all data?");
            input = cin.nextLine();
        }
    }

    private static void createCustomer(){
        System.out.println("Provide the customer's name: ");             //Simply gather the information of the new customer
        String name = cin.nextLine();
        System.out.println("Enter the name of the store the customer is going to from the following list: ");
        printStores();       //print a list of stores for the new customer to choose from
        String store = cin.nextLine();
        for (Customer c : customers){     //check every customer already in the database
            if (name.equals(c.getCustomerName())){ //if this is the same customer,
                if (getStoreNum(store)!= -1){             //send them to the new store
                    stores.get(getStoreNum(store)).addCustomer(c);
                    return;             //and end the createCustomer() flow
                }
            }
        }
        System.out.println("What is the customer's budget?");
        double budget = cin.nextDouble();
        cin.nextLine(); //To eat the newline characters that nextDouble doesn't grab
        System.out.println("Is the customer wearing a mask? (Y/N)");
        boolean masked = cin.nextLine().equals("Y");
        Customer shopper = new Customer(name, budget, masked);  //Create the customer,
        customers.add(shopper);                                 //Add him to the master list of customers,
        if (getStoreNum(store) != -1){                    // get the index of the right store
            stores.get(getStoreNum(store)).addCustomer(shopper);  //and send the customer to it
        }

    }
    private static void createStore(){
        System.out.println("Enter the name of the store to create: ");
        String input = cin.nextLine();          //create a new store from the name,
        boolean add = true;
        for (RetailStore store : stores){        //and check if it already exists
            if (store.getName().equals(input)){
                add = false;
            }
        }
        if (add){
            stores.add(new RetailStore(input));    //if it does not exist, make it and add it to the list of stores
        }
        else{
            System.out.println("This store already exists, please try again.");
        }
    }
    private static void createItem(){
        System.out.println("Enter the name of the item: ");
        String name = cin.nextLine();                     //Gather some information about the item
        System.out.println("Enter the price of the item: ");
        double price = cin.nextDouble();
        System.out.println("Enter the quantity available: ");
        int quantity = cin.nextInt();
        cin.nextLine();  //Again taking the newline characters that nextInt doesn't grab
        System.out.println("Enter the name of the store you would like to add the item to. Registered stores are as follows: ");
        printStores();
        String storeName = cin.nextLine();
        if (getStoreNum(storeName) != -1){             //and just like for the customers, get the right store index
            stores.get(getStoreNum(storeName)).addItem(name,price,quantity);
        }
    }


    private static int getStoreNum(String name){
        for (int i = 0; i < stores.size(); i++){          //cycle through each store, if the given name matches, return that store index
            if (stores.get(i).getName().equals(name)){    //I chose to return the index of the store rather than the store object itself
                return i;                                 //because it makes error checking a little easier if the store doesn't exist
            }
        }
        return -1;                                          //return -1 if there are no stores with that name
    }
    private static void dummyData(){                      //This is the dummy data to make testing easier, it's two stores with some different items
        stores.add(new RetailStore("Taco Bell"));
        stores.get(0).addItem("Taco", 1.99, 10);
        stores.get(0).addItem("Burrito", 2.49, 8);         //can you tell I was hungry while doing this lab?
        stores.add(new RetailStore("Juanita's"));
        stores.get(1).addItem("Chimichanga", 2.99, 12);
        stores.get(1).addItem("Quesadilla", 0.99, 15);
        customers.add(new Customer("Bob", 30, true));     //create a couple different customers, all wearing masks or else they wouldn't
        customers.add(new Customer("Ava", 14, true));     //be in the stores. Store(0) has just one customer, Store(1) has 4 so
        customers.add(new Customer("Eve", 22, true));     //it's easier to test the 5 person maximum rule.
        customers.add(new Customer("Ivi", 20, true));
        customers.add(new Customer("Ovo", 99, true));

        stores.get(0).addCustomerDummy(customers.get(0)); // and add each customer to their respective store
        stores.get(1).addCustomerDummy(customers.get(1));
        stores.get(1).addCustomerDummy(customers.get(2));
        stores.get(1).addCustomerDummy(customers.get(3));
        stores.get(1).addCustomerDummy(customers.get(4));

    }
    private static void printStores(){    //This is just an easier way of displaying each store
        if (stores.size() == 0) return;
        String prnt = "";
        for (RetailStore st : stores){
            prnt += st.getName() + ", ";
        }
        System.out.println(prnt.substring(0,prnt.length()-2)); //the substring cuts off the last comma
    }
    private static void printAll(){  //And this displays every customer and store, better visualizing the result of the program operation
        System.out.println("All customer information: ");
        for (Customer c : customers){
            System.out.println("Name: " + c.getCustomerName() + ", Budget: " + c.getBudget() + ", masked? " + c.isWearingMask() + ", Receipts: " + c.getReceipts());
        }
        System.out.println("All store information: ");
        for (RetailStore s : stores){
            System.out.println("Name: " + s.getName() + ", Current Shoppers: \r\n" + s.getCustomers());
        }

    }

    public static void main(String[] args) {
        displayMenu();
    }
}
