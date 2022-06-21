package rclauss.c212.lab6;

public abstract class Athlete extends Person{
    protected String athleteId;
    protected String athleteTeam;
    protected String athleteType;
    public abstract String toString();
    public abstract int getTotalTimePlayed();
    
    public Athlete(String firstName, String lastName, String birthDate, String athleteId, String athleteTeam, String athleteType){
        super(firstName, lastName, birthDate);
        this.athleteId = athleteId;
        this.athleteTeam = athleteTeam;
        this.athleteType = athleteType;
    }

    public Athlete(){
        super();
        this.athleteId = "0";
        this.athleteTeam = "Team";
        this.athleteType = "Sport";
    }

    public String getAthleteId(){
        return athleteId;
    }
    public void setAthleteId(String aId){
        athleteId = aId;
    }
    public String getAthleteTeam(){
        return athleteTeam;
    }
    public void setAthleteTeam(String aTeam){
        athleteTeam = aTeam;
    }
    public String getAthleteType(){
        return athleteType;
    }
    public void setAthleteType(String aType){
        athleteType = aType;
    }
}