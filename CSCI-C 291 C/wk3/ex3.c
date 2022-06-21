//Q.3). The total distance traveled by vehicle in ‘t’ seconds is given by
//distance=(ut)+0.5(a)(t^2) where ‘u’ and ‘a’ are the initial velocity (m/sec)
//and acceleration (m/sec^2). Write a C program using a function called
//‘distCalc()’ that takes in the integer values of ‘u’, ‘a’ and ’t’ and returns
//the distance covered by the vehicle to the main program where you must print
//its value.(The logic to calculate the distance must be in the distCalc()
//function and the returned value must be printed in the main() function).


#include <stdio.h>

int distCalc(int u, int a, int t);

int main(void){
  int velocity,acceleration,time = 0;
  printf("Input initial velocity:\n");
  scanf("%d", &velocity);
  printf("Input acceleration:\n");
  scanf("%d", &acceleration);
  printf("Input time: \n");
  scanf("%d", &time);
  printf("Distance traveled: %d\n", distCalc(velocity,acceleration,time));
}


int distCalc(int u, int a, int t){
  return ((u*t)+((a/2)*(t*t)));
}
