package rclauss.c212.lab5;

import java.util.Scanner;
import java.util.ArrayList;

public final class StudentDirectory{

    public StudentDirectory(){}

    //ID AGE YEAR GRADE

    public static Integer[][] students = {{1,15,9,90},
                                          {2,18,12,50},
                                          {3,17,11,85},
                                          {4,16,11,100},
                                          {5,15,10,80},
                                          {6,16,10,70},
                                          {7,15,9,100},
                                          {8,18,12,90}};
    public static void main(String[] args){
        Scanner cin = new Scanner(System.in);
        System.out.println("Search the directory by entering the minimum value of each variable, or enter -1 to skip: ");
        System.out.print("Minimum age: ");
        int age = cin.nextInt();
        System.out.print("Minimum Year(9-12): ");
        int year = cin.nextInt();
        System.out.print("Minimum Grade(0-100): ");
        int grade = cin.nextInt();
        System.out.print("ID's of returned students: ");
        for (Integer i : search(age, year, grade)) {
            System.out.print(i + " ");
        }
        cin.close();
    }


    public static Integer[] search(int age, int year, int grade){
        ArrayList<Integer> retID = new ArrayList<Integer>();
        boolean searchAge = true ? age != -1 : false;
        boolean ageAdd = false;
        boolean searchYear = true ? year != -1 : false;
        boolean yearAdd = false;
        boolean searchGrade = true ? grade != -1 : false;
        boolean gradeAdd = false;
        int iter = 0;
        for (int i = 0;i<students.length;i++){
            ageAdd = true ? searchAge == false || students[i][1] >= age : false;
            yearAdd = true ? searchYear == false || students[i][2] >= year : false;
            gradeAdd = true ? searchGrade == false || students[i][3] >= grade : false;
            if (ageAdd && yearAdd && gradeAdd){
                retID.add(iter++, students[i][0]);
            }
        }
        return retID.toArray(new Integer[0]);
    }

}