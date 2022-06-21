package rclauss.c212.lab6;

public final class SoccerAthlete extends Athlete{

    private String arenaType;
    private int numOfHalves;
    private int minutesPerHalf;

    public SoccerAthlete(String fName, String lName, String bDate, String aId, String aTeam, String athType, String aType, int nOfHalves, int mPerHalf){
        super(fName, lName, bDate, aId, aTeam, athType);

        arenaType = aType;
        numOfHalves = nOfHalves;
        minutesPerHalf = mPerHalf;
    }
    public SoccerAthlete(){
        super();
        arenaType = "Stadium";
        numOfHalves = 0;
        minutesPerHalf = 0;
    }
    @Override
    public String toString() {
        return Integer.toString(getTotalTimePlayed());
    }
    @Override
    public int getTotalTimePlayed() {
        return numOfHalves * minutesPerHalf;
    }
    public String getArenaType(){
        return arenaType;
    }
    public void setArenaType(String aType){
        arenaType = aType;
    }
    public int getNumOfHalves(){
        return numOfHalves;
    }
    public void setNumOfHalves(int nOfHalves){
        numOfHalves = nOfHalves;
    }
    public int getMinutesPerHalf(){
        return minutesPerHalf;
    }
    public void setMinutesPerHalf(int mPerHalf){
        minutesPerHalf = mPerHalf;
    }
    
}