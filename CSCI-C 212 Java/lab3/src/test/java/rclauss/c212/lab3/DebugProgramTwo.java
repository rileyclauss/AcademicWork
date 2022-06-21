package rclauss.c212.lab3;
//  Lab 3
//
//  Released:  9/8/2021
//
//  @Author  Riley Clauss rclauss
//  Last Edited: 1/27/2021
//
//
//  Directions: The given file is not according to java coding guidelines
//              and may have compilation errors to be fixed. 
//              Tasks to be performed:
//              1. Edit the file to make it according to java coding guidelines 
//              and fix the errors if any.
//              2. Include comments to indicate the changes made to the file 
//              to make it according to coding conventions or fix issues.
//
//////////////////////////////////////////////////////////////////////////////



/*

Note: The file is a standalone java file, meaning you can run this file directly without having to set up the other 2 files.

About the java file: The current Program computes Area of different shapes based on user input.

User Input: 
1. choice: User should enter either 1 or 2 depending on which shape the user wants to compute area for.
2. base, height for triangle and radius for circle: The lengths of shapes for which areas must be computed.

Expected Program Output:
The correct result for this program

Eg: 

Find area of 
1 . Triangle 
2 . Circle 
Select a choice : 1
Enter the length of base : 
2
Enter the length of height : 
2
Area of triangle with length of sides 2 and 2 is : 2
*/
import java.io.*;
import java.util.Scanner;//added missing import
class DebugProgramTwo
{
    public void findarea(int a, int b)
    {
        double area = ( a*b) / 2 ;  
        System.out.println( "\n Area of triangle with length of sides "+a+ " and " +b+" is : "+ area);
    }
  
    public void findarea(int a){
    System.out.println( "\n Area of circle with  radius " +a+ " is :" + 3.14 * a);
    }

    public void main(String p[]) throws IOException{
      DebugProgramTwo d = new DebugProgramTwo();
      Scanner keyboard = new Scanner(System.in);
      System.out.print("\n Find area of \n 1 . Triangle \n 2 . Circle \n\nSelect a choice : ");
      int choice = keyboard.nextInt();
 
      if(choice == 1){ //changed selection type
         System.out.print("\n Enter the length of base : ");
         int x =keyboard.nextInt();//fixed missing space
         System.out.print("\n Enter the length of height : ");
         int y = keyboard.nextInt(); //corrected Syntax of line
         findarea(x,y); //fixed spelling error
         
      }
      else if (choice == 2){
         System.out.print("\n Enter the radius : ");
         int r =keyboard.nextInt();
         d.findarea(r);
      }
      else  {
         System.out.println("Invalid choice");
      }
   
   }
} // fixed missing brace
