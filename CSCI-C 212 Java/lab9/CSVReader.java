import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

/*

1. Open and read the products.csv file from the zip folder 
2. Compute the following: 
• Average price for each product category 
• Most expensive product amongst products listed 
• Count of products for each product category 
*/



public class CSVReader{
//hair, office, school, clothing
    public static void main(String[] args){
    
        Scanner cin;
        try{
            cin = new Scanner(new File("products.csv"));        //try creating a new Scanner on the csv file
            cin.nextLine();                                     //skip the heading
        }catch (Exception e){
            System.out.println("Exception occurred: " + e.getMessage());
            return;     //if anything precludes the Scanner from being created, exit execution
        }
        List<List<String>> records = new ArrayList<List<String>>();     //make a new list of lists of records
        while(cin.hasNextLine()){
            records.add(Arrays.asList(cin.nextLine().split(",")));      //and load each value in, splitting on the commas
        }
        Integer count[] = {0,0,0,0,0};                                  //count of each product, including a 5th category for non-enumerated categories
        String expensive[] = {"","","","",""};                          //array of names of the most expensive products
        Double expensiveCost[] = {0.0,0.0,0.0,0.0,0.0};                 //array of cost for the most expensive products
        Double avgPrice[] = {0.0,0.0,0.0,0.0,0.0};                      //collection of average prices
        for (int i = 0; i<records.size();i++){              //for each record, 
            try{
                if (records.get(i).get(1).equals("school_supplies")){       //if it's a school supply,
                    avgPrice[0] += tryDouble(records.get(i).get(2));        //add to the counter for average prices
                    if (tryDouble(records.get(i).get(2)) > expensiveCost[0]){   //if it's more expensive than the previously most expensive product,
                        expensive[0] = records.get(i).get(0);                   //set the expensive variables to reflect that
                        expensiveCost[0] = tryDouble(records.get(i).get(2));    
                    }
                    count[0]++;                                                 //and increase the counter for that product
                }
                else if (records.get(i).get(1).equals("hair_health_beauty")){   //do the same for Hair, Health, and Beauty products,
                    avgPrice[1] += tryDouble(records.get(i).get(2));
                    if (tryDouble(records.get(i).get(2)) > expensiveCost[1]){
                        expensive[1] = records.get(i).get(0);
                        expensiveCost[1] = tryDouble(records.get(i).get(2));
                    }
                    count[1]++;
                }
                else if (records.get(i).get(1).equals("office_supplies")){      //office supplies, 
                    avgPrice[2] += tryDouble(records.get(i).get(2));
                    if (tryDouble(records.get(i).get(2)) > expensiveCost[2]){
                        expensive[2] = records.get(i).get(0);
                        expensiveCost[2] = tryDouble(records.get(i).get(2));
                    }
                    count[2]++;
                }
                else if (records.get(i).get(1).equals("clothing")){             //clothing, 
                    avgPrice[3] += tryDouble(records.get(i).get(2));
                    if (tryDouble(records.get(i).get(2)) > expensiveCost[3]){
                        expensive[3] = records.get(i).get(0);
                        expensiveCost[3] = tryDouble(records.get(i).get(2));
                    }
                    count[3]++;
                }
                else{                                                           //and any non-enumerated categories
                    System.out.println("Misc");
                    avgPrice[4] += tryDouble(records.get(i).get(2));
                    if (tryDouble(records.get(i).get(2)) > expensiveCost[4]){
                        expensive[4] = records.get(i).get(0);
                        expensiveCost[4] = tryDouble(records.get(i).get(2));
                    }
                    count[4]++;
                }
            }catch (Exception e){                                               //if anything happens, reflect it to the user
                System.out.println("Exception encountered: " + e.getMessage());
            }
        }
        for (int j = 0;j<5;j++){                                                //calculate the average price for all 5 categories
            try{
                if (count[j] == 0.0) throw new ArithmeticException("Divide by zero.");  //if the count of a category is 0, throw an exception
                avgPrice[j] = avgPrice[j]/ count[j];                                    //store average price
            }catch (ArithmeticException e){
                avgPrice[j] = 0.0;                                                      //if the count is 0, set the average price to 0 rather than NaN which is the standard
            }
            
        }

        //print the values of everything calculated
        System.out.printf("Average price for School Supplies: $%.2f\nAverage price for Hair, Health, and Beauty: $%.2f\nAverage price for Office Supplies: $%.2f\nAverage price for Clothing: $%.2f\nAverage price for miscellaneous: $%.2f\n", avgPrice[0], avgPrice[1], avgPrice[2], avgPrice[3], avgPrice[4]);
        System.out.printf("Most expensive School Supplies product: %s @ $%.2f\nMost expensive Hair, Health, and Beauty product: %s @ $%.2f\nMost expensive Office Supplies product: %s @ $%.2f\nMost expensive Clothing product: %s @ $%.2f\nMost expensive Miscellaneous product: %s @ $%.2f\n", expensive[0], expensiveCost[0],expensive[1], expensiveCost[1],expensive[2], expensiveCost[2],expensive[3], expensiveCost[3],expensive[4], expensiveCost[4]);
        System.out.printf("Number of School Supplies products: %d\nNumber of Hair, Health, Beauty products: %d\nNumber of Office Supplies products: %d\nNumber of Clothing products: %d\nNumber of Miscellaneous products: %d\n", count[0],count[1],count[2],count[3],count[4]);
    }

    public static Double tryDouble(String dub) throws NumberFormatException{
        try{            //try to parse a double from the 3rd column value
            return Double.parseDouble(dub);
        }catch(NumberFormatException e){        //which will throw a NumberFormatException
            System.out.println("Exception encountered with " + dub + e.getMessage());   //print that, and
        }
        return 0.0;                                                                     //return 0.0
    }

}