package rclauss.c212.lab7;

public class Item{
    private String name;          //Items have a name, price, and quantity
    private double price;         //I decided to include the quantity of an item in the Item class, so multiple of the same item wouldn't have to be
    private int quantity;         //created in memory and all chained together; instead the quantity allows for more efficient storage

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return this.price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getQuantity() {
        return this.quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public Item(String name, double price, int quantity){
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
}
