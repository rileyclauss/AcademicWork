#include <stdio.h>
#define SIZE 50

void reverse(const char * const inp);
int main(void){

    char input[SIZE];
    printf("Enter a string of maximum size %d characters: ", SIZE);
    fgets(input, SIZE, stdin);  //using fgets to get a string of a maximum size rather than scanf
    char *iPtr = input;         //declare a pointer to the char array
    reverse(iPtr);              //call the recursive function to print the string in reverse order
    int sum = -1;               //sum is -1 to keep the \0 char from being counted
    for (;*iPtr != '\0';++iPtr){
        sum++;
    }
    printf("\nLength of string: %d\n", sum);
    return 0;
}
void reverse(const char * const inp){
    if (inp[0] == '\0')    //at the end of the given string, 
        return;             //return and print all characters
    else{
        reverse(&inp[1]);   //other wise recurse
        printf("%c", inp[0]);   //and the last char is printed first, the first char printed last
    }
}
