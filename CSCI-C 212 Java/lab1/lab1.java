public class lab1{

    public static void main(String[] args){
        System.out.println("(a)");  //Printing pattern A
        for (int i = 1;i<=10;i++){
            for (int j = 1;j<=i;j++){  //Using a nested for loop to 
                System.out.print("*");  //Print number of asterisk equal to line number
            }
            System.out.println();
        }
        System.out.println("(b)");
        for (int i = 10;i>=0;i--){  //using a nested for loop
            for (int j = 0;j<=i;j++){  //with a reversed top loop to
                System.out.print("*"); //print in reverse
            }
            System.out.println();
        }
        System.out.println("(c)");
        for (int i = 0;i<=10;i++){ //printing number of asterisks
            for (int j = 0; j < i; j++){ //and compensating spaces first
                System.out.print(" ");  
            }
            for (int k = 10;k>=i;k--){
                System.out.print("*");
            }
            System.out.println();
        }
        System.out.println("(d)");  //doing the same as pattern c
        for (int i = 0;i<=10;i++){  //but in reverse
            for (int k = 10;k>=i;k--){
                System.out.print(" ");
            }
            for (int j = 0; j < i; j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}