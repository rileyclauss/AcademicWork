#include <stdio.h>  
int main() { 

    int a = 0;
    printf("Please ,input variable a\n"); 
    scanf("%d", &a); 
    printf("a: %d\n", a); 
    return 0; 
} 

//Using the backtrace command, GDB shows that an error is occuring because
//of the scanf statement on line 6. This shows that the scanf statement
//is improperly formatted, the a variable needs to be prefixed with an &
