#include <stdio.h>

int main(void){
  int size = 0;
  printf("Please input the size of the array: \n");
  scanf("%d", &size);
  int array[size];
  printf("Please enter the elements of the array: \n");
  for (int i = 0;i < size;i++)
    scanf("%d", &array[i]);
  int max = 0;
  int min = array[0];
  int sum = 0;
  for (int i = 0;i<size;i++){
    printf("%d\n", array[i]);
    if (max < array[i])
      max = array[i];
    if (min > array[i])
      min = array[i];
    sum += array[i];
  }
  printf("Largest value is %d, smallest value is %d, sum is %d\n", max,min,sum);
}

