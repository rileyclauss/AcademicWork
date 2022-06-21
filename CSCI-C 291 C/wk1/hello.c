/* 
 * Problem 1 Code 
 * Author: Riley Clauss
*/

#include <stdio.h>

int main(void) {
  char city[20];
  char name[20];
  printf("Enter your name: ");
  scanf("%s", name);
  printf("Enter your city: ");
  scanf("%s", city);  
  printf("Hello: Welcome to C291!\nThis is %s\nI live in %s\n", name, city);
  return(0); 
}
