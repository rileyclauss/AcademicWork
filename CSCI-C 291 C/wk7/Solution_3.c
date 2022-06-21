#include <stdio.h>

int main(void){

    int input = 0;
    printf("Enter an integer: ");           //take an integer input
    scanf("%d", &input);
    int count = 0;              
    while (input > 0){                      //as long as it's greater than 0
        if (input & 1){                     //if the LSB is 1, add to the count
            count++;
        }
        input = input>>1;                   //right shift it no matter what
    }
    printf("%d set bits.\n", count);          //and print the result
}
