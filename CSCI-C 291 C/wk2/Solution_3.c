#include <stdio.h>

int main(void){

	int input;
	int multi = 0;
	printf("Enter a number:\n");

	scanf("%d", &input);
	while (input <= 100){
	
		printf("%d ",input);
		input *= multi;

	}
	printf("\n");
}
