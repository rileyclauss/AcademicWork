import java.util.ArrayList;

public class AmusementParkExample{

    public static void main(String[] args){

        AmusementPark funLand = new AmusementPark();        //a new amusement park
    
        Ride r1 = new Ride("Red Roller", 2, true);          //with two rides, the first supporting fast pass
        Ride r2 = new Ride("Blue Blaze", 3, false);         //and the second not supporting fast pass

        funLand.rides.add(r1);                              //add them to the list of rides
        funLand.rides.add(r2);                              //which is public purely for convenience and appearance of code

        ArrayList<Customer> ride1list = new ArrayList<Customer>();
        ride1list.add(new Customer("Bob Dylan", true));     //create a list of riders to be added
        ride1list.add(new Customer("Ringo Starr", false));
        ride1list.add(new Customer("George Harrison", true));
        ride1list.add(new Customer("Paul McCartney", true));
        ride1list.add(new Customer("John Lennon", false));
        ride1list.add(new Customer("Julian Casablancas", true));
        ride1list.add(new Customer("Fabrizio Moretti", false));
        ride1list.add(new Customer("Albert Hammond Jr.", false));
        ride1list.add(new Customer("Nikolai Fraiture", true));
        ride1list.add(new Customer("Nick Valensi", false));
        funLand.rides.get(0).addToQueue(ride1list);
        ArrayList<Customer> ride2list = new ArrayList<Customer>();
        ride2list.add(new Customer("Ringo Dylan", true));
        ride2list.add(new Customer("George Starr", false));
        ride2list.add(new Customer("Paul Harrison", true));
        ride2list.add(new Customer("John McCartney", true));
        ride2list.add(new Customer("Julian Lennon", false));
        ride2list.add(new Customer("Fabrizio Casablancas", true));
        ride2list.add(new Customer("Albert Moretti", false));
        ride2list.add(new Customer("Nikolai Hammond Jr.", false));
        ride2list.add(new Customer("Nick Fraiture", true));
        ride2list.add(new Customer("Bob Valensi", false));
        funLand.rides.get(1).addToQueue(ride2list);
        funLand.printMe();
        System.out.println("--------------------Run the Red Roller--------------------");
        funLand.rides.get(0).Run();  //the first run should provide the first two fast pass riders, Bob Dylan and George Harrison
        funLand.printMe();
        System.out.println("--------------------Run the Blue Blaze--------------------");
        funLand.rides.get(1).Run(); //and this should provide the first three riders, regardless of fastpass
        funLand.printMe();          //who are Ringo Dylan, George Starr, and Paul Harrison
        System.out.println("--------------------Empty the Red Roller--------------------");
        funLand.rides.get(0).Run();
        funLand.rides.get(0).Run(); 
        funLand.rides.get(0).Run();
        funLand.rides.get(0).Run();
        funLand.printMe();
        System.out.println("--------------------Empty the Blue Blaze--------------------");
        funLand.rides.get(1).Run();
        funLand.rides.get(1).Run();
        funLand.rides.get(1).Run();
        funLand.printMe();
    }

}