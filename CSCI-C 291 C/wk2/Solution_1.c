#include <stdio.h>
#include <stdbool.h>
int main(void){

    int operand1, operand2;
    char operator;
    _Bool running = true;
    while (running == true){
      printf("Enter your desired operation. (+ for addition, - for subtraction, * for multiplication, / for division, or Q to quit)\n");
      scanf(" %c", &operator);
      if (operator == 'Q'){
      	printf("Thank you for using my calculator.\n");
	running = false;
	break;
      }
      printf("Enter the operands for this equation:\n");
      scanf("%d, %d", &operand1, &operand2);
      switch (operator){
        case '+':
          printf("%d\n", operand1 + operand2);
          break;
        case '-':
          printf("%d\n", operand1-operand2);
          break;
        case '*':
          printf("%d\n", operand1*operand2);
          break;
        case '/':
          if (operand2>0){
            printf("%d\n", operand1/operand2);
          }
          else{
            printf("Cannot divide by zero.\n");
          }
          break;
        default:
          printf("Invalid operand, %d,  try again.\n", operator);
          break;
      }
        
    }
  
}
