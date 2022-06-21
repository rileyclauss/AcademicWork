import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class IOReader {

    static final String FILENAME = "students.txt";

    static File record;        //declare variables above methods to be able to access them anywhere
    static Scanner cin;        //but I declare each one inside of each method, just to make handling exceptions a bit cleaner
    static PrintWriter pw;     
    static ArrayList<String> recs;
    public static void main(String[] args) throws IOException {
        recs = new ArrayList<String>();                 //declare a new arraylist of each line to be able to rewrite it later, updated in updateList() method
        Scanner scan = new Scanner(System.in);
        boolean exit = false;
        String inp;
        while (!exit){
            updateList();                               //read and store the file as it is now
            System.out.println("Menu: 1. Add a student, 2. Delete a student by name, 3. Count of all students by class, 4. Total count of students, 5. Exit.");
            inp = scan.nextLine();                      //take new input
            switch (inp){
                case "1":
                    System.out.println("Enter the name of the student, press enter, and then enter F, s, J, or S to reflect class standing.");
                    addStudent(scan.nextLine(), scan.nextLine());      //take the input of the name and the year to pass to addStudent
                    break;
                case "2":
                    System.out.println("Enter the name of the student you would like to delete: ");
                    deleteStudent(scan.nextLine());         //Take the name of the student to delete
                    break;
                case "3":
                    countStudents();
                    break;
                case "4":
                    System.out.println("Total number of students: " + recs.size());     //Simply call .size() for the record ArrayList which will always be up to date when called
                    break;
                case "5":
                    exit = true;
                    break;
            }
        }
        scan.close();
        pw.close();
    }

    public static void updateList() throws IOException{
        try{
            record = new File(FILENAME);          //updating the list with a file that doesn't exist will throw a FileNotFound exception
            cin = new Scanner(record);                  
        }catch (IOException e){
            System.out.println("ERROR: The provided file does not exist, it will be created. Proper execution is not guaranteed");
            return;                                     //If the file doesn't exist, a print writer will create a file of that name.
        }
        recs.clear();                           //empty the records as they are now,
        while (cin.hasNextLine()) {
            recs.add(cin.nextLine());           //and refill them with each line
        }
    }

    public static void addStudent(String name, String year) throws IOException {
        try {
            record = new File(FILENAME);        //try to make a file and PrintWriter
            pw = new PrintWriter(record);
        } catch (IOException e) {
            e.printStackTrace();
        }
        for (int i=0;i<recs.size();i++){
            pw.println(recs.get(i));            //reprint each record, since it's been cleared by pw
        }
        pw.println(year + " " + name);          //finally, add the year and name of the new student
    }

    public static void deleteStudent(String name) throws IOException {
        try {
            record = new File(FILENAME);        //set up a scanner and a print writer
            cin = new Scanner(record);
            pw = new PrintWriter(record);
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }
        for (int i = 0; i < recs.size(); i++) {
            if (!recs.get(i).contains(name)) {
                pw.println(recs.get(i));            //print every record that doesn't match the name of who is to be deleted
            }
        }
    }

    public static void countStudents() throws FileNotFoundException {
        try{
            record = new File(FILENAME);        //set up a scanner
            cin = new Scanner(record);
        }catch (FileNotFoundException e){
            e.printStackTrace();
            return;
        }
        String input = "";
        Integer count[] = {0,0,0,0};
        while(cin.hasNextLine()){
            input = cin.nextLine();             //take each line,
            if (input.charAt(0) == 'F'){        //compare the first character to the known class standings
                count[0]++;
            }
            else if(input.charAt(0) == 's'){
                count[1]++;
            }
            else if(input.charAt(0) == 'J'){
                count[2]++;
            }
            else if(input.charAt(0) == 'S'){
                count[3]++;
            }
        }                                       //and then print them out
        System.out.printf("Freshman: %d Sophomore: %d Junior: %d Senior: %d\n", count[0], count[1], count[2], count[3]);
    }
}