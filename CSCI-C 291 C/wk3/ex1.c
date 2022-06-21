//Q.1) Writea function in C programming to find all the prime numbers between
//two intervals using ‘functions’.(You should take lower and upper limit values as
//input from the user and pass these values to a function like ‘primeNum()’ which
//calculates and prints the prime numbers in between those two numbers)

#include <stdio.h>

void primeNum(int upper, int lower);

int main(void){
        int lowerlimit = 0;
        int upperlimit = 0;
        printf("Input lower limit: \n");
        scanf("%d", &lowerlimit);
        printf("\nInput upper limit: \n");
        scanf("%d", &upperlimit);
	primeNum(upperlimit,lowerlimit);
}

void primeNum(int upper, int lower){
  printf("\nPrime numbers: \n");
  int factors = 0;
        if(lower < upper) {
                for(int i = lower; i<=upper; i++) {
			factors = 0;
                  for (int j = 1;j<i;j++){
                      if (i%j == 0){
                        factors++;
                      }
                  }
                  if (factors == 1){
                    printf("%d ", i);
                  }
                }
        }
        
	printf("\n");
}
