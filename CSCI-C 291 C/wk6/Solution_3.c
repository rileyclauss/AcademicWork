#include <stdio.h>
#include <stdlib.h>

void swap(float * a, float * b);
int main(void){
    float *aPtr = (float*)malloc(sizeof(float));
    float *bPtr = (float*)malloc(sizeof(float));
    printf("Enter number A to swap: ");
    scanf("%f", aPtr);
    printf("Enter number B to swap: ");
    scanf("%f", bPtr);
    swap(aPtr,bPtr);
    printf("Values after swapping: a = %.2f, b = %.2f\n", *aPtr, *bPtr);

    free(aPtr);
    free(bPtr);
}
void swap(float * a, float * b){
    *a = *a + *b;    //combine A and B to get AB
    *b = *a - *b;    //subtract B from AB to get A
    *a = *a - *b;    //subtract A from AB to get B
}
