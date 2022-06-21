#include <stdio.h>
#include <stdlib.h>

int main(void){

    int size = 0;
    printf("Enter the size of the array: ");
    scanf("%d", &size);             
    int * array = (int*)malloc(sizeof(int)*size);       //declare an array of the desired size
    int i = 0;
    for (i=0;i<size;i++){
        printf("Enter element %d: ", i);                //take each element input
        scanf(" %d", &array[i]);
    }
    int j = 0;
    for (i = 0;i<size-1;i++){                       //loop through each element, except for the last one
        for (j=i+1;j<size;j++){                     //loop through each element after the element at i
            if ((array[i] ^ array[j]) == 0){        //if they are the same as each other, XOR will produce 0000
                printf("%d\n", array[i]);             //print that value, which is the same for array[i] and array[j]
            }
        }
    }
}
