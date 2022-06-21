#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){

    int *inputs;
    int num = 0;
    printf("Enter the number of elements you would like to input: ");
    scanf("%d", &num);                                                      //get the number of integers to be input
    inputs = (int *)malloc(sizeof(int)*num);                                //declare an array of that size
    int i = 0;
    for(i=0;i<num;i++){
        printf("Enter input %d: ",i);                                       //take each integer from the user
        scanf("%d", &inputs[i]);
    }
    int j = 0;
    int andCount = 0, orCount = 0, xorCount = 0;
    for (i=0;i<num-1;i++){
        for (j=i+1;j<num;j++){
            if ((inputs[i] & 1)&&(inputs[j]&1)){//if the least significant bit (1) is equal
                andCount++;                                                 //and not 0
            }
            if ((inputs[i] & 1) || (inputs[j]&1)){                          //if either are true (1)
                orCount++;
            }
            if ((inputs[i]&1) != (inputs[j]&1)){                            //if they are not equal
                xorCount++;
            }
        }
    }
    char * andPairs = (char*)malloc(sizeof(" (00,00)") * andCount);         //now that we know how many pairs there are,
    char * orPairs = (char*)malloc(sizeof(" (00,00)") * orCount);           //we can dynamically allocate memory to array of characters
    char * xorPairs = (char*)malloc(sizeof(" (00,00)") * xorCount);         //for cleaner printing later on
    char temp[10];
    for (i=0;i<num-1;i++){                                                  //run back through the array
        for (j=i+1;j<num;j++){
            if ((inputs[i] & 1)==(inputs[j]&1)){
                sprintf(temp," (%2d,%2d)", inputs[i],inputs[j]);            //and for each pair, add them to 
                strcat(andPairs, temp);                                     //the strings declared above with some formatting
            }
            if ((inputs[i] & 1) || (inputs[j]&1)){
                sprintf(temp," (%2d,%2d)", inputs[i],inputs[j]); 
                strcat(orPairs, temp);
            }
            if ((inputs[i]&1) != (inputs[j]&1)){
                sprintf(temp," (%2d,%2d)", inputs[i],inputs[j]); 
                strcat(xorPairs, temp);
            }
        }
    }
    printf("Total AND pairs: %d, %s\n", andCount, andPairs);
    printf("Total OR pairs: %d, %s\n", orCount, orPairs);               //then print each category of pair
    printf("Total XOR pairs: %d, %s\n", xorCount, xorPairs);
    free(andPairs);
    free(orPairs);              //and free all allocated memory
    free(xorPairs);
    free(inputs);
}
