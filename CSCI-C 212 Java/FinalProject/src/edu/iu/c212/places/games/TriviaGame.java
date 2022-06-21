package edu.iu.c212.places.games;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.*;

import edu.iu.c212.Arcade;
import edu.iu.c212.models.User;
import edu.iu.c212.utils.ConsoleUtils;
import edu.iu.c212.utils.http.HttpUtils;
import edu.iu.c212.utils.http.TriviaQuestion;

public class TriviaGame extends Game {


    public TriviaGame(Arcade arcade){
        super.placeName = "Trivia";
        super.entryFee = 0.0;
        super.arcade = arcade;
    }


    @Override
    public void onEnter(User user) {
        user.setBalance(user.getBalance()-this.entryFee);   //entry fee is taken and saved to file
        try {
            arcade.saveUsersToFile();
        } catch (IOException e1) {
            e1.printStackTrace();
        }
        System.out.println("Welcome to C212 trivia. You get $2 for each correct answer - there are 5 total questions in this trivia round.");
        List<TriviaQuestion> questions = new ArrayList<TriviaQuestion>();   //create a list
        try {
            questions = HttpUtils.getTriviaQuestions(5);        //and populate it with five random questions
        } catch (IOException e) {
            e.printStackTrace();
        }
        int rightAnswers = 0;       //count the number of correct answers
        String ans;
        for (int i = 0;i<5;i++){
            System.out.println("You're on question " + (i+1) + ". Ready?");
            List<String> options = new ArrayList<String>(questions.get(i).getIncorrectAnswers());   //populate the options with the incorrect answers
            options.add(questions.get(i).getCorrectAnswer());   //add the correct answer
            Collections.shuffle(options);                       //then shuffle all the options
            ans = ConsoleUtils.printMenuToConsole(questions.get(i).getQuestion(), options, true);   //get a response from the player
            if (ans.equals(questions.get(i).getCorrectAnswer())){       //if they're correct, 
                System.out.println("You got it right! You got $2.");
                user.setBalance(user.getBalance()+2.0);                 //give the reward and save to the file
                rightAnswers++;         //I prefer adding and saving the reward every time
                try {                   //rather than at the end to ensure each answer gets a reward even if the program crashes
                    arcade.saveUsersToFile();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            else{               //If the user gets the wrong answer, notify them
                System.out.println("You got it wrong :( The correct answer is: "+questions.get(i).getCorrectAnswer());
            }
        }
        //Display how many right answers the user provided, either encouragingly or disappointedly
        System.out.println(rightAnswers>2?"Nice! You got " + rightAnswers + " questions right." : "Aww, good try. You got " + rightAnswers + " questions right.");
        //Then return the user to the lobby
        System.out.println("Returning to the lobby...");
        arcade.transitionArcadeState("Lobby");
    }
}
