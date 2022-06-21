#include <stdio.h> 
int sum(int n)  {  
    int i; 
    int result = 0; 
    for (i = 1; i <= n; i++) { 
    result += i; 
    }  
    return result; 
} 

int main() { 
    int n; 
    printf("Enter n value: "); 
    scanf("%d", &n); 
    printf("Sum of n natural numbers is: %d\n", sum(n)); 
    return 0; 
} 
//Using GDB I can see that result, before the for loop in sum() has even been run, has an 
//arbitrary value, meaning its location in memory had not been initialized. 
//the error can be fixed by initializing the result variable.
