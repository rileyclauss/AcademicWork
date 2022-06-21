import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

class BankAccount{

    public ArrayList<String> transactions;


    BankAccount(String fileName){
        this.transactions = new ArrayList<String>();
        try{
            File file = new File(fileName);
            Scanner cin = new Scanner(file);
            while (cin.hasNextLine()){
                transactions.add(cin.nextLine());
            }
            cin.close();
        }catch(Exception e){
            System.out.println("Error occurred, please try again.");
            return;
        }
    }

    public static void main(String[] args){
    
        BankAccount bank = new BankAccount("transactions.txt");
        HashMap<String,Integer> localAcc = new HashMap<String,Integer>();
        localAcc = currentBalances(bank.transactions);
        for (String i : localAcc.keySet()){
            System.out.println(i + ": " + localAcc.get(i));
        }
        System.out.println("\nUpdate balance: ");
        localAcc = updateBalances(localAcc);
        for (String i : localAcc.keySet()){
            System.out.println(i + ": " + localAcc.get(i));
        }
    }

    static HashMap<String,Integer> currentBalances(ArrayList<String> trans){
        String line[];
        HashMap<String,Integer> accounts = new HashMap<String,Integer>();
        for (String i : trans){
            line = i.split(",");
            if (accounts.keySet().contains(line[0])){
                if (line[2].equals("d")){
                    accounts.put(line[0], accounts.get(line[0]) + Integer.parseInt(line[1]));
                }
                else if(line[2].equals("w")){
                    accounts.put(line[0], accounts.get(line[0]) - Integer.parseInt(line[1]));
                }
            }
            else{
                if (line[2].equals("d")){
                    accounts.put(line[0], Integer.parseInt(line[1]));
                }
                else if (line[2].equals("w")){
                    accounts.put(line[0], -1 * Integer.parseInt(line[1]));
                }
            }
            
        }
        return accounts;
    }

    static HashMap<String,Integer> updateBalances(HashMap<String,Integer> accounts){
        for (String i : accounts.keySet()){
            if (accounts.get(i) >= 1500) accounts.put(i, accounts.get(i) + 100);
        }
        return accounts;
    }

}