package rclauss.c212.lab6;

public final class HockeyAthlete extends Athlete{

    private String arenaType;
    private int numOfPeriods;
    private int minutesPerPeriod;

    public HockeyAthlete(String fName, String lName, String bDate, String aId, String aTeam, String athType, String aType, int nOfPeriods, int mPerPeriod){
        super(fName, lName, bDate, aId, aTeam, athType);

        arenaType = aType;
        numOfPeriods = nOfPeriods;
        minutesPerPeriod = mPerPeriod;
    }
    public HockeyAthlete(){
        super();
        arenaType = "Stadium";
        numOfPeriods = 0;
        minutesPerPeriod = 0;
    }
    @Override
    public String toString() {
        return Integer.toString(getTotalTimePlayed());
    }
    @Override
    public int getTotalTimePlayed() {
        return numOfPeriods * minutesPerPeriod;
    }
    public String getArenaType(){
        return arenaType;
    }
    public void setArenaType(String aType){
        arenaType = aType;
    }
    public int getNumOfPeriods(){
        return numOfPeriods;
    }
    public void setNumOfPeriods(int nOfPeriods){
        numOfPeriods = nOfPeriods;
    }
    public int getMinutesPerPeriod(){
        return minutesPerPeriod;
    }
    public void setMinutesPerQuarter(int mPerPeriod){
        minutesPerPeriod = mPerPeriod;
    }
    
}