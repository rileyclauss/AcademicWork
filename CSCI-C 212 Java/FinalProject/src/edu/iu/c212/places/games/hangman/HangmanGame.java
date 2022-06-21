package edu.iu.c212.places.games.hangman;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import edu.iu.c212.Arcade;
import edu.iu.c212.models.User;
import edu.iu.c212.places.games.Game;
import edu.iu.c212.utils.ConsoleUtils;
import edu.iu.c212.utils.http.HttpUtils;


public class HangmanGame extends Game implements IHangmanGame{



    public HangmanGame(Arcade arcade){
        super.arcade = arcade;
        super.placeName = "Hangman";
        super.entryFee = 5.0;
    }


    @Override
    public void onEnter(User user) {
        user.setBalance(user.getBalance()-this.entryFee);   //take the entry fee and save
        try {
            arcade.saveUsersToFile();
        } catch (IOException e1) {
            e1.printStackTrace();
        }
        System.out.println("Welcome to Hangman! This game picks a random word, and you have to guess it letter by letter. If you guess a wrong letter 6 times, you lose! If you win, you get $15.");
        String secretWord = null;   //The secret word is the un-blurred word to be guessed
        int badGuesses = 0;         //this counts how many letters not in the word have been guessed
        char guess;                 //and the user-given guess
        boolean stillGuessing = true;
        try {
            secretWord = HttpUtils.getRandomHangmanWord();
        } catch (IOException e) {
            e.printStackTrace();
        }
        List<Character> guesses = new ArrayList<Character>();   //this tracks every guess so far
        while(stillGuessing){
            System.out.println("You've guessed " + badGuesses + " times incorrectly. " + guessesToString(guesses));
            System.out.println("The word is: " + getBlurredWord(guesses, secretWord));
            System.out.println("Please enter a character from the following lexicon that you have not already guessed: ");
            System.out.println(getValidLexicon());
            guess = ConsoleUtils.readLineFromConsole().toLowerCase().charAt(0); //read the character given to the console, made to lowercase
            if(getValidLexicon().contains(guess)){      //if it's in the lexicon (any letter)
                if(secretWord.contains(String.valueOf(guess))){ //and if it's in the secret word, 
                    guesses.add(guess);                         //add it to the guesses and do nothing else
                }
                else{       //if it's not in the secret word, tell the user
                    System.out.println(guess +  " is not in the secret word.");
                    guesses.add(guess); //add it to the guesses
                    badGuesses++;       //and increment the number of bad guesses
                }
            }
            else{   //or if it's not in the lexicon, 
                System.out.println("Your input is invalid. Please enter a character from the provided list.");
                badGuesses++;   //count it as a bad guess but don't add it to the guesses list
            }

            if (getBlurredWord(guesses, secretWord).equals(secretWord)){    //if getBlurredWord returns the whole word, then the word has been guessed
                System.out.println("Congrats, you won with " + badGuesses + " incorrect guesses! You got $15");
                user.setBalance(user.getBalance()+15.0);    //add to the user's balance
                try {
                    arcade.saveUsersToFile();               //save it to the file, and continue
                } catch (IOException e) {
                    e.printStackTrace();
                }
                stillGuessing = false;
            }
            if (badGuesses > 5 && stillGuessing == true){   //If the word hasn't been found and the user is out of guesses,
                System.out.println("Sorry, you didn't guess the word in time. The secret word was " + secretWord);
                stillGuessing = false;      //end the game
            }
        }
        System.out.println("Returning to the lobby...");    //then return to the lobby
        arcade.transitionArcadeState("Lobby");
    }


    @Override
    public String getBlurredWord(List<Character> guesses, String word) {
        String retStr = "";
        for (char c : word.toCharArray()){  //for each character in the string
            if (guesses.contains(c)){       //if it's in guesses
                retStr += c;                //add it to the return string
            }
            else{
                retStr += '*';              //otherwise add * in its place
            }
        }   //So, as stated above, if the user guesses every character in the word, it should return the word itself and will
            //of course be equal
        return retStr;
    }


    @Override
    public List<Character> getValidLexicon() {
        List<Character> x = new ArrayList<Character>();
        for(int i = 0; i < 26; i++){    //This returns all 26 lowercase letters
            x.add((char)(97 + i));
        }
        return x;
    }
    public String guessesToString(List<Character> guesses){
        String retString = "[ ";    //This method returns a displayable string of every guess given so far
        for (char c : guesses){
            retString += (c + " ");
        }
        return retString+"]";
    }
}
