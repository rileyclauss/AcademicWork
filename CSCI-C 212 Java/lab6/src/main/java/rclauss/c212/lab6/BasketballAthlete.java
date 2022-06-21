package rclauss.c212.lab6;

public final class BasketballAthlete extends Athlete{

    private String arenaType;
    private int numOfQuarters;
    private int minutesPerQuarter;

    public BasketballAthlete(String fName, String lName, String bDate, String aId, String aTeam, String athType, String aType, int nOfQuarters, int mPerQuarter){
        super(fName, lName, bDate, aId, aTeam, athType);

        arenaType = aType;
        numOfQuarters = nOfQuarters;
        minutesPerQuarter = mPerQuarter;
    }
    public BasketballAthlete(){
        super();
        arenaType = "Stadium";
        numOfQuarters = 0;
        minutesPerQuarter = 0;
    }
    @Override
    public String toString() {
        return Integer.toString(getTotalTimePlayed());
    }
    @Override
    public int getTotalTimePlayed() {
        return numOfQuarters * minutesPerQuarter;
    }
    public String getArenaType(){
        return arenaType;
    }
    public void setArenaType(String aType){
        arenaType = aType;
    }
    public int getNumOfQuarters(){
        return numOfQuarters;
    }
    public void setNumOfQuarters(int nOfQuarters){
        numOfQuarters = nOfQuarters;
    }
    public int getMinutesPerQuarter(){
        return minutesPerQuarter;
    }
    public void setMinutesPerQuarter(int mPerQuarter){
        minutesPerQuarter = mPerQuarter;
    }
    
}