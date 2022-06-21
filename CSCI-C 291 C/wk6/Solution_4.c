#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define SIZE 10    //change size as needed.

void sortAscending(int * arr);
void sortDescending(int * arr);
void swap(int * a, int * b);
int main(void){
    int i = 0;
    int *array = (int*)malloc(SIZE*sizeof(int)); //create an array of SIZE elements
    printf("Enter %d elements: ", SIZE);
    for (i = 0; i<SIZE;i++){
        scanf("%d", &array[i]);         //loop through and take each one
    }
    int *ascendArray = &array[0];       //create different arrays for ascension and descension
    int *descendArray = &array[0];
    sortAscending(ascendArray);         //sort the ascending array
    printf("Ascending: ");
    for (i = 0; i<SIZE;i++){
        printf("%d ", ascendArray[i]);  //and print it
    }
    sortDescending(descendArray);       //sort the descending array
    printf("\nDescending: ");
    for (i = 0; i<SIZE;i++){
        printf("%d ", descendArray[i]);  //and print it
    }
    printf("\n");
}
void sortAscending(int * arr){
    bool wholePass = false;                     //if the loop makes it all the way through without swapping, it is sorted
    int i = 0;
    while(!wholePass){                          //without making a full pass, run again
        wholePass = true;                       //hope that this pass is complete
        for (i = 0; i<SIZE-1;i++){              //for each element,
            if (arr[i] > arr[i+1]){             //if the one after it is larger, 
                wholePass = false;
                swap(&arr[i],&arr[i+1]);        //swap them
            }
        }
    }
}
void sortDescending(int * arr){
    bool wholePass = false;
    int i = 0;
    while(!wholePass){                          //same as above,
        wholePass = true;
        for (i = 0; i<SIZE-1;i++){
            if (arr[i] < arr[i+1]){             //but if the next element is smaller
                wholePass = false;
                swap(&arr[i],&arr[i+1]);
            }
        }
    }
}
void swap(int * a, int * b){
    *a = *a + *b;
    *b = *a - *b;                               //same as Solution_3
    *a = *a - *b;
}
