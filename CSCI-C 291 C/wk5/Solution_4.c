#include <stdio.h>
#include <stdbool.h>

int main(void){
    char time[11];                                          //Because the format is known, the size of the array is 11
    bool complete = false;                                  //bool to loop until a proper input is given
    printf("Enter the time in hh:mm:ssAM/PM format: "); 
    while (!complete){                                      //while a good input has not been entered,
        scanf( "%11s", time);                               //take the input
        if (time[2] ==58 && time[5] == 58){//if the 3rd and 6th values are colons, reasonably assume the array is correct.
            complete = true;                                //If it's not correct, it's the users fault at that point, right?
        }
        else if(time == "fun fact"){                        
            printf("Did you know that AM is short for the latin ante meridiem, meaning 'before midday,' \nand PM is short for post meridiem, meaning 'after midday?'\n");
        }
        else{                                               //If an improperly formatted input is given, prompt the user again.
            printf("Please enter the time in the correct format of hh:mm:ssAM/PM\n");
        }
    }

    if (time[8] == 65 || time[8] == 97){   //if the 9th char is 'A' or 'a', it's AM and can be printed as is
        if (time[0] == '1' && time[1] == '2'){  //unless it's midnight, in which case hh = 00
            printf("The time in 24hr format is 00%c%c%c%c%c%c.\n",time[2],time[3],time[4],time[5],time[6],time[7]);
        }
        else printf("The time in 24hr format is %c%c%c%c%c%c%c%c.\n",time[0],time[1],time[2],time[3],time[4],time[5],time[6],time[7]);
    }
    else{
        int hh = ((time[0]-48)*10) + (time[1]-48);  //hh is the int value of the first two characters
        if(hh<12){          //if it's greater than 12 (not noon and before one), add 12
            hh += 12;
        }
        printf("The time in 24hr format is %d%c%c%c%c%c%c.\n",hh,time[2],time[3],time[4],time[5],time[6],time[7]);  //and print
    }
    
    
}
