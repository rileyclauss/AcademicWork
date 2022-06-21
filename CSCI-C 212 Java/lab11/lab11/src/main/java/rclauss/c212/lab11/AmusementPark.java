package rclauss.c212.lab11;
import java.util.ArrayList;
import java.util.List;

public class AmusementPark{

    public List<Ride> rides;

    public AmusementPark(){
        rides = new ArrayList<Ride>();          //list of rides, arbitrarily set to an ArrayList
    }

    public void printMe(){
        System.out.println("Rides: ");
        for (Ride r : rides){
            System.out.println("   " + r.getName() + ":");
            System.out.println("      " + r.getCapacity() + " max");
            System.out.println("      " + r.que.size() + " waiting now");
        }
    }
}