#include <stdio.h>
#include <stdbool.h>
int main(void){

	char food;
	bool hereortogo;
	int temp;
	printf("Enter the dish you would like: B for burritos, T for Tacos, and N for Nachos: \n");
	scanf(" %c", &food);
	printf("For here (0) or to go(1)?\n");
	scanf("%d", &temp);
	hereortogo = temp;
	if (hereortogo == true){
		printf("To go with ");
	}
	else{
		printf("For here with ");
	}
	switch (food){
		case 'B':
			printf("Burritos\n");
			break;
		case 'T':
			printf("Tacos\n");
			break;
		case 'N':
			printf("Nachos\n");
			break;
	}
}
