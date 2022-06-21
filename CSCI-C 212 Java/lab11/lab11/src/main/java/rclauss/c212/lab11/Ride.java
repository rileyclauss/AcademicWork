package rclauss.c212.lab11;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

public class Ride{

    private String name;
    private int capacity;
    private int ticketNum;
    public Queue<Customer> que;

    public Ride(String name, int capacity, Boolean fastPassCompatible) {
        this.name = name;
        this.capacity = capacity;
        if(fastPassCompatible) que = new PriorityQueue<Customer>();     //If it supports fastpass, make it a priority queue
        else que = new LinkedList<Customer>();                          //otherwise, a linked list (purely FIFO) works fine for this purpose
    }


    public void Run(){
        int i = 0;
        System.out.print("Removed from queue: ");
        Customer nxt;
        for (i=0;!que.isEmpty() && i< capacity;i++){                //as long as there are riders waiting and we're not at capacity
            nxt = que.poll();                                       //get the next customer, remove him from the queue
            System.out.print(""+nxt.getName() + (nxt.getFastPass()?"[F], ":", "));  //and print his name and fastpass status, denoted by a [F]
        }
        System.out.println("");
    }
    public void addToQueue(List<Customer> add){
        Customer x;
        while(!add.isEmpty()){          //while there are customers to be added
            x = add.get(0);             //get the next customer
            x.place = this.ticketNum++; //assign him a place value to force PriorityQueue to respect FIFO for equally compared elements
            que.add(x);                 //add them to the queue
            add.remove(0);              //and remove them from the waiting list
        }
    }


    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getCapacity() {
        return this.capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }



    
}