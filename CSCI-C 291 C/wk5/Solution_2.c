#include <stdio.h>
#include <ctype.h>

int const LENGTH = 50;

int main(void){
    char str[LENGTH];       //String to take the input
    printf("Enter the string from which you would like to sum numbers: ");
    scanf("%s", str);
    int sum = 0;     //intialize the sum
    int strLen = 0;  //and the length
    for (int i = LENGTH-1;i>=0;i--){
        if (str[i]-0 == 0){           //start at the end, find the first endline character
            strLen = i;
        }
    }
    for (int i = 0; i<strLen;i++){    //iterate just over the entered portion of the string
        if (isdigit(str[i])){           //if it's a digit, add it to the sum
            sum += (str[i]-'0');        //minus the ASCII int value of 0 to convert it to a usable value
        }
    }
    printf("The sum is: %d.\n", sum);
}
