#include <stdio.h>
#include <stdlib.h>

float add(float * a, float * b);
float subtract(float * a, float * b);
float multiply(float * a, float * b);
float divide(float * a, float * b);
int main(void){

    float *aPtr = (float*)malloc(sizeof(float));  //allocate a pointer of the first and second operands
    float *bPtr = (float*)malloc(sizeof(float));  //don't need an actual variable, just a pointer and memory
    char operation;
    printf("Enter the first operand: ");
    scanf("%f", aPtr);
    printf("Enter the second operand: ");
    scanf("%f", bPtr);
    printf("Enter the operation (+, -, *, /): ");
    scanf(" %c", &operation);
    float result = 0;               //prepare to take the result
    switch (operation){     //switch on user input for operation
        case '+':
            result = add(aPtr, bPtr);
            printf("%.2f %c %.2f = %.2f\n", *aPtr, operation, *bPtr, result);
            break;
        case '-':
            result = subtract(aPtr, bPtr);
            printf("%.2f %c %.2f = %.2f\n", *aPtr, operation, *bPtr, result);
            break;
        case '*':
            result = multiply(aPtr,bPtr);
            printf("%.2f %c %.2f = %.2f\n", *aPtr, operation, *bPtr, result);
            break;
        case '/':
            result = divide(aPtr, bPtr);
            printf("%.2f %c %.2f = %.2f\n", *aPtr, operation, *bPtr, result);
            break;
        default:   //
            printf("\nInvalid operation.\n");
    }
    free(aPtr);
    free(bPtr);
}
float add(float * a, float * b){
    return (*a)+(*b); //add the values
}
float subtract(float * a, float * b){
    return (*a)-(*b);  //subtract the values
}
float multiply(float * a, float * b){
    return (*a)*(*b); //multiply the values
}
float divide(float * a, float * b){
    return (*a)/(*b); //divide the values
}
