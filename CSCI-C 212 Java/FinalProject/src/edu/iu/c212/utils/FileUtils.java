package edu.iu.c212.utils;

import edu.iu.c212.models.Item;
import edu.iu.c212.models.User;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class FileUtils {
    private static File file = new File("userInfo.txt");

    // line format:
    // user_name|balance|item1,item2,item3
    // user name not allowed to contain pipe

    /**
     * Write user data to the file you provided above.
     *
     * @param users The total list of all users
     */
    public static void writeUserDataToFile(List<User> users) throws IOException {
        PrintWriter cout = new PrintWriter(new FileWriter(file, false));
        String writeLine;
        for (User u : users){
            writeLine = "";
            writeLine += u.getUsername()+"|"+u.getBalance()+"|";
            for(Item i : u.getInventory()){
                writeLine += i.toString()+",";
            }
            cout.println(writeLine.substring(0,writeLine.length()-1));
        }
        cout.close();
    }

    /**
     * Read user data from the file you provided above. Return a list of Users
     */
    public static List<User> getUserDataFromFile() throws IOException {
        List<User> retList = new ArrayList<>();
        List<String> input;
        Scanner cin = new Scanner(file);
        List<Item> inventory = new ArrayList<>();
        User u;
        while(cin.hasNext()){
            inventory.clear();
            input = Arrays.asList(cin.next().split("\\|"));
            for (String i : input.get(2).split(",")){
                inventory.add(Item.findByKey(i.substring(0,i.indexOf("-"))));
            }
            u = new User(input.get(0),Double.parseDouble(input.get(1)));
            for(Item i : inventory){
                u.addItem(i);
            }
            retList.add(u);
            
        }
        return retList;
    }
}
