// Q.2) Writea program in C to find the Greatest Common Divider(GCD) of two
//numbers using ‘recursion’.(User gives the two numbers as input which are
//passed to some function called ‘findGCD()’ where the main logic of the program
//is supposed to be written. Remember this has to be a recursive function. The
//function must finally return the calculated value to the main() function
//where it must be then printed.)

#include <stdio.h>

int findGCD(int div1, int div2);

int main(void){
  int divisor1, divisor2 = 0;
  printf("Input divisor 1:\n");
  scanf("%d", &divisor1);
  printf("Input divisor 2:\n");
  scanf("%d", &divisor2);
  printf("GCD of %d and %d is %d\n", divisor1,divisor2,findGCD(divisor1,divisor2));
}


int findGCD(int div1, int div2){
  //q1 = q2 * somenum + remainder
  //when remainder is 0, return q2, else, q1=q2,q2=r
  if (div1 == 0){
    return div2;
  }
  else{
    return findGCD(div2%div1, div1);
  }
  

}
