package edu.iu.c212.places.games;

import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

import edu.iu.c212.Arcade;
import edu.iu.c212.models.User;

public class GuessTheNumberGame extends Game{


    public GuessTheNumberGame(Arcade arcade){
        super.placeName = "Guess the Number";
        super.arcade = arcade;
        super.entryFee = 5.0;
    }

    @Override
    public void onEnter(User user) {
        user.setBalance(user.getBalance()-this.entryFee);    //take the entry fee and save
        try {
            arcade.saveUsersToFile();
        } catch (IOException e1) {
            e1.printStackTrace();
        }
        System.out.println("Welcome to Guess the Number. You will be guessing a number between 1 and 100 (inclusive).");
        System.out.println("You have five guesses, if you get it right you will get $10.");
        Random rand = new Random();
        int r = rand.nextInt(100);   //create a random number between 0-99 inclusive
        r++;    //then add one to it, making the possible numbers 1-100 inclusive
        boolean playing = true;
        Scanner cin = new Scanner(System.in);
        int guesses = 1, guess = 0; //holds number of guesses, and the newest guess
        while(playing == true && guesses <= 5){     //if guesses exceed 5 before the number is guessed, playing stays true
            System.out.println("Enter guess " + guesses);
            guess = cin.nextInt();
            if (guess == r){    //if the user guesses correctly
                guesses++;
                playing = false;    //the game ends
                System.out.println("Congratulations! You guessed the number. You won $10!");
                user.setBalance(user.getBalance()+10.0); //the user is paid their reward
                try {
                    arcade.saveUsersToFile();           //and gets saved to file
                } catch (IOException e) {
                    e.printStackTrace();
                }

            }
            else if (guess > r){        //if the guess is too high, notify the user and increment guesses
                System.out.println("Your guess was too high.");
                guesses++;
            }
            else{
                guesses++;              //likewise if it's too low
                System.out.println("Your guess was too low.");
            }
        }
        if(playing == true){        //if playing is still true, the user did not guess the number, and therefore lost
            System.out.println("Sorry, you were not able to guess the number in time.");
        }
        System.out.println("Returning to the lobby...");    //the user is then returned to the lobby
        arcade.transitionArcadeState("Lobby");
    }

    @Override
    public String toString() {
        return super.toString();
    }


}
