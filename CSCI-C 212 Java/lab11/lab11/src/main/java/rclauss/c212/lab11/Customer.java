package rclauss.c212.lab11;
public class Customer implements Comparable<Customer> {

    private String name;            //Store the customer's name
    private Boolean fastPass;       //whether they own a fastpass,
    public int place;               //and their place in line

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Boolean getFastPass() {
        return this.fastPass;
    }

    public void setFastPass(Boolean fastPass) {
        this.fastPass = fastPass;
    }

    public Customer(String name, Boolean fastPass){
        this.name = name;
        this.fastPass = fastPass;
    }

    @Override
    public int compareTo(Customer that) {
        int ret = (this.getFastPass() ? -1 : 0);        //if this has a fast pass and that does't, prioritize the smalles with -1
        ret += (that.getFastPass() ? 1 : 0);            //This can be represented by the decision table below
        if (ret == 0){      //if both customers have or don't a fastpass, then priority queue does not properly replace
            if (this.place < that.place) return -1; //the lower priority elements - high priority elements don't then necessarily
            else return 1;                          //follow FIFO - this hacky ID system fixes that by putting the first high priority element first
        }
        return ret;
    }
                                                            /*
                                                            this   that
                                                            0   +   0 = 0
                                                            0   +   1 = 1
                                                            -1  +   0 = -1
                                                            -1  +   1 = 0
                                                            */
}