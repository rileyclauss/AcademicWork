#include <stdio.h>
#include <stdbool.h>
int SIZE = 0;
double matrix[100][100]; //matrix of arbitrary size, since no len function exists for arrays
void printArray(double[100][100], int); //only used for debugging
int gaussElimination(double[100][100]);  //prototyping gaussian elimination with double matrix as division is used
int main(void){
    int rows, columns;
    bool complete = false; //boolean for if valid input has been entered
    printf("This program calculates the determinant of square matricies.\n");
    while (!complete){
        printf("Enter the number of rows: \n");
        scanf("%d", &rows);
        printf("Enter the number of columns: \n");
        scanf("%d", &columns);
        if (columns == rows) //if a square matrix has been entered, exit while loop
            complete = true;
        else{
            printf("The number of rows and columns must be equal to calculate the determinant.\n");
        }
    }
    SIZE = rows;
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < columns;j++){
            printf("Enter element for X%d%d: ", i,j);
            scanf("%lf", &matrix[i][j]); //enter double for each index in matrix
        }
    }
    printf("Determinant = %d\n", gaussElimination(matrix));
}

void printArray(double arr[100][100], int sze){
    for (int i = 0; i < sze;i++){
        printf("print array %d [ ", i);
        for (int j = 0; j<sze;j++){
            printf("%d ", arr[i][j]);
        }
        printf("]\n");
    }
}

int gaussElimination(double array[100][100]){
    double determinant = 1;
    for (int i = 0;i<SIZE;++i){
        bool zeroCol = false; //boolean for column of zero
        if (array[i][i] == 0){  //if index 0 is 0,
            zeroCol = true;
            for (int j = i;j<SIZE;++j){ //check each index under it
                if (array[j][i]!=0){    //if there is a value, swap
                    determinant *= -1;  //flip determinant
                    for (int k = 0;k<SIZE;++k){
                        double swapInt = array[i][k]; //and switch 1 column with another
                        array[i][k] = array[j][k];
                        array[j][k] = swapInt;
                        zeroCol = false;  //making zerocol false
                    }
                }
            }
        }
        if (zeroCol == true){ //but if every element is 0, determinant is 0
            determinant = 0;
            break;
        }
        else{
            for (int j = i+1;j<SIZE;++j){ //for next row,
                double swapInt = array[j][i];
                for (int k = i;k<SIZE;++k){
                    array[j][k] -= (array[i][k]*swapInt)/array[i][i]; // eliminate based off of pivot
                }
            }
            determinant *= array[i][i];  //and take next step of determinant
        }
    }
    return determinant;
}
