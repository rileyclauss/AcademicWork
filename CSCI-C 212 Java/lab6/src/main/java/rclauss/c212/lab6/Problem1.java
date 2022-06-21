package rclauss.c212.lab6;

import java.util.Scanner;

/**
 * Hello world!
 */
public final class Problem1 {
    private Problem1() {
    }
    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        String fName,lName,bDate; // strings for Person class
        String athId,athTeam,athType; // strings for Athlete class
        String aType; // string and generic ints for quarters/periods/halves ; resolved by athType
        int nOfRounds, mPerRound; 
        System.out.println("Enter first name:");
        fName = cin.nextLine();
        System.out.println("Enter last name:");
        lName = cin.nextLine();
        System.out.println("Enter birthdate (mm/dd/yyyy):");
        bDate = cin.nextLine();
        System.out.println("Enter athlete ID:");
        athId = cin.nextLine();
        System.out.println("Enter athlete team:");
        athTeam = cin.nextLine();
        System.out.println("Enter athlete type:");
        athType = cin.nextLine();
        System.out.println("Enter the arena type: ");
        aType = cin.nextLine();
        System.out.println("Enter number of halves/quarters/periods:");
        nOfRounds = cin.nextInt();
        System.out.println("Enter minutes played per half/quarter/period:");
        mPerRound = cin.nextInt();
        switch(athType){
            case("Basketball"):
                BasketballAthlete b = new BasketballAthlete(fName, lName, bDate, athId, athTeam, athType, aType, nOfRounds, mPerRound);
                System.out.println("Total time played: " + b.toString() + " minutes.");
                break;
            case("Hockey"):
                HockeyAthlete a = new HockeyAthlete(fName, lName, bDate, athId, athTeam, athType, aType, nOfRounds, mPerRound);
                System.out.println("Total time played: " + a.toString() + " minutes.");
                break;
            case("Soccer"):
                SoccerAthlete s = new SoccerAthlete(fName, lName, bDate, athId, athTeam, athType, aType, nOfRounds, mPerRound);
                System.out.println("Total time played: " + s.toString() + " minutes.");
                break;
        }
        cin.close();
    }
}
