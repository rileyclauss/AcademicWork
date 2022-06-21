#include <stdio.h>

int const LENGTH = 50;

int main(void){
    char str[LENGTH];   //declare string of length LENGTH
    int numChar;        //and an int to take the size of the string
    printf("Enter the length of the string: ");
    scanf("%d", &numChar);   //take the length of the string
    printf("Enter the string you would like to count of Hs and Is: ");
    scanf("%s", str);        //and take the string
    int numH = 0;           //count of Hs
    int numI = 0;           //and count of Is
    for (int i = 0; i<numChar;i++){   //iterate over every char
        if (str[i] == 'H'){         //if it's an H, add to H count
            numH++;                 
        }
        else if (str[i] == 'I'){    //add to I count if it's I
            numI++;
        }
        else{
            printf("A character that is not H or I was entered. Correct program execution is not guaranteed.");   //general error
        }
    }
    if (numI < numH){                                             //If there are fewer Is, the number of chars to change is = to number of Is
        printf("%d characters must be changed.\n", numI);
    }   
    else {                                                          //Same for if there are fewer Hs
        printf("%d characters must be changed.\n", numH);
    }
}

