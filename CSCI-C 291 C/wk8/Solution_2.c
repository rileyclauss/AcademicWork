#include <stdlib.h>
#include <stdio.h>

int main(void){

    int *aPtr;
    aPtr = (int*)malloc(sizeof(int));
    double *bPtr;
    bPtr = (double*)malloc(sizeof(double)*2);
    int *cPtr;
    cPtr = (int*)malloc(sizeof(int)*5);
    int i;
    for (i=0;i<5;i++){
        *(cPtr + i) = i;
        printf("%i", *(cPtr+i));
    }
    printf("\n");
    free(aPtr);
    free(bPtr);
    free(cPtr);
}
