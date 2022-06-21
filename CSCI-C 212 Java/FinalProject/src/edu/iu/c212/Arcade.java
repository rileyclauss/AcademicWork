package edu.iu.c212;

import edu.iu.c212.models.User;
import edu.iu.c212.places.Inventory;
import edu.iu.c212.places.Lobby;
import edu.iu.c212.places.Place;
import edu.iu.c212.places.Store;
import edu.iu.c212.places.games.GuessTheNumberGame;
import edu.iu.c212.places.games.TriviaGame;
import edu.iu.c212.places.games.blackjack.BlackjackGame;
import edu.iu.c212.places.games.hangman.HangmanGame;
import edu.iu.c212.utils.FileUtils;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Arcade implements  IArcade {

    User currentUser;
    List<User> allUsers;
    List<Place> allPlaces;

    public Arcade(){
        try {           //this loads all users already saved in file, to make sure returning players are recognized
            allUsers = new ArrayList<User>(FileUtils.getUserDataFromFile());
        } catch (IOException e) {
            e.printStackTrace();
        }
        currentUser = getUserOnArcadeEntry();   //this asks the user to input their username
        allPlaces = new ArrayList<Place>();     //this initializes the list of places, filled below
        Lobby lobby = new Lobby(this);
        Inventory inventory = new Inventory(this);
        Store store = new Store(this);
        TriviaGame triviaGame = new TriviaGame(this);
        BlackjackGame blackjackGame = new BlackjackGame(this);
        HangmanGame hangmanGame = new HangmanGame(this);
        GuessTheNumberGame guessTheNumberGame = new GuessTheNumberGame(this);
        allPlaces.add(lobby);
        allPlaces.add(inventory);
        allPlaces.add(store);
        allPlaces.add(triviaGame);
        allPlaces.add(blackjackGame);
        allPlaces.add(hangmanGame);
        allPlaces.add(guessTheNumberGame);

        transitionArcadeState("Lobby"); //and transitions to the lobby
    }
    public User getCurrentUser(){
        return this.currentUser;
    }
    @Override
    public List<User> getUserSaveDataFromFile() throws IOException {
        return FileUtils.getUserDataFromFile();
    }

    @Override
    public void saveUsersToFile() throws IOException {
        FileUtils.writeUserDataToFile(allUsers);        //this is called whenever a player earns or spends money
    }

    @Override
    public void transitionArcadeState(String newPlaceNameToGoTo) {
        int goTo = 0;       //default to the lobby destination, so if anything goes wrong they come back to the Places menu
        if(newPlaceNameToGoTo.contains("Inventory")){
            goTo = 1;
        }
        else if(newPlaceNameToGoTo.contains("Store")){
            goTo = 2;
        }
        else if(newPlaceNameToGoTo.contains("Trivia")){
            goTo = 3;
        }
        else if(newPlaceNameToGoTo.contains("Blackjack")){
            goTo = 4;
        }
        else if(newPlaceNameToGoTo.contains("Hangman")){
            goTo = 5;
        }
        else if(newPlaceNameToGoTo.contains("Guess")){
            goTo = 6;
        }
        else if(newPlaceNameToGoTo.contains("Exit")){
            System.out.println("Goodbye!");
            try {
                saveUsersToFile();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return;
        }
        else{
            System.out.println("Please enter a number corresponding to one of the places above.");
        }
        //The user is sent to their destination -- the goTo var corresponds to each place in the allPlaces list
        //so, of course, 0 is the lobby, 1 is the Inventory, etc.
        allPlaces.get(goTo).onEnter(currentUser);

    }

    @Override
    public User getUserOnArcadeEntry() {
        Scanner cin = new Scanner(System.in);
        System.out.println("Enter your username: ");
        String name = cin.next();
        Boolean newUser = true; //assume it's a new user,
        for (User u : allUsers){
            if (name.equals(u.getUsername())){  //unless the given username matches a name in the file
                currentUser = u;
                System.out.println("Welcome back!");    //then welcome the user back and do nothing
                newUser = false;
            }
        }
        if (newUser){   //If it is a new user, create the new user as the current user and add them to the list
            System.out.println("Welcome to the arcade!");
            currentUser = new User(name,0);
            allUsers.add(currentUser);
        }
        return currentUser;
    }

    @Override
    public List<Place> getAllPlaces() {
        return allPlaces;
    }
}
