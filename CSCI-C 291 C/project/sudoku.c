
#include <stdio.h>
#include <stdlib.h>

int stepOne();
int stepTwo();
int stepThree();
void insertSudoku();
void printSudoku();
int columnCheck(int,int);
int rowCheck(int,int);
int gridCheck(int,int,int);
int checkSolved();
int solveSudoku(int,int);
int partialSolveSudoku(int,int);
int sudokuCells[9][9];


int stepOne(){
    printf("Step 1: Insert values and print the puzzle.\n");
    insertSudoku();
    printSudoku();
}
int stepTwo(){
    printf("Step 2: Partially solve the sudoku.\n");
    partialSolveSudoku(0,0);
    printSudoku();
}
int stepThree(){
    printf("Step 3: Solve the entire sudoku.\n");
    insertSudoku();
    solveSudoku(0,0);
    printSudoku();
}
void insertSudoku(){
    int i, j;
    for (i = 0;i<9;i++){    // Iterate over every row and column to initialize each cell to 0
        for (j = 0;j<9;j++){
            sudokuCells[i][j] = 0;
        }
    }
    // Insert each value into its corresponding cell
    sudokuCells[0][0] = 2;
    sudokuCells[0][6] = 6;
    sudokuCells[0][7] = 9;
    sudokuCells[1][1] = 5;
    sudokuCells[1][5] = 3;
    sudokuCells[2][0] = 1;
    sudokuCells[2][1] = 7;
    sudokuCells[2][5] = 9;
    sudokuCells[2][6] = 4;
    sudokuCells[2][8] = 5;
    sudokuCells[3][2] = 3;
    sudokuCells[3][4] = 2;
    sudokuCells[3][5] = 5;
    sudokuCells[3][7] = 1;
    sudokuCells[3][8] = 8;
    sudokuCells[4][4] = 4;
    sudokuCells[5][0] = 7;
    sudokuCells[5][1] = 2;
    sudokuCells[5][3] = 3;
    sudokuCells[5][4] = 8;
    sudokuCells[5][6] = 5;
    sudokuCells[6][0] = 5;
    sudokuCells[6][2] = 2;
    sudokuCells[6][3] = 6;
    sudokuCells[6][7] = 4;
    sudokuCells[6][8] = 1;
    sudokuCells[7][3] = 5;
    sudokuCells[7][7] = 7;
    sudokuCells[8][1] = 6;
    sudokuCells[8][2] = 7;
    sudokuCells[8][8] = 3;
}
void printSudoku(){
    int i,j;
    for (i=0;i<9;i++){  //iterate over each row
        if (i%3 == 0){  //if it's a border row (0, 3, or 6) print a topline border
            printf("-------------------------\n");
        }
        //then print each row with dividers
        printf("| %d %d %d | %d %d %d | %d %d %d | \n", sudokuCells[i][0], sudokuCells[i][1], sudokuCells[i][2], sudokuCells[i][3],sudokuCells[i][4],sudokuCells[i][5], sudokuCells[i][6],sudokuCells[i][7],sudokuCells[i][8]);
    }
    printf("-------------------------\n");
}

int rowCheck(int row, int num){
    int i;  //i iterates over each column in the given row
    for (i = 0; i < 9; i++){
        if (sudokuCells[row][i] == num){        //if the given number is already in the row, 
            return 0;                           //return 0 
        }
    }
    return 1;   //if the given number is not already in the row, return 1
}

int columnCheck(int col, int num){
    int i;  //same as above, but i iterates over each row in the given column
    for (i = 0; i < 9; i++){    //for each row in the column
        if (sudokuCells[i][col] == num){    //if the number is already used
            return 0;                       //return 0
        }
    }
    return 1;   //if the given number is not already in the column, return 1
}
int gridCheck(int row, int col, int num){
    int rowStart = row - (row%3);   //rowStart and colStart represent the top left cell of a given grid
    int colStart = col - (col%3);   //so any cell can be calculated to their square with this modulus
    int i,j;
    for (i=0;i<3;i++){              //then, iterate over the first, second, and third row in the grid
        for(j=0;j<3;j++){           //and the first, second, and third cell (or column) in that row
            if (sudokuCells[rowStart+i][colStart+j] == num){    //if the number is in use,
                return 0;                                       //return 0
            }
        }
    }   //otherwise, the given number is not in the grid, so return 1
    return 1;
}

int partialSolved(){ 
    //this function is for step 2, checking if three squares have been solved yet
    int i,j,solvedSquares=0;
    for (i=0;i<3;i++){              //for each row of grids
        for (j=0;j<3;j++){          //and each column of grids in each row,
            if (gridCheck(i*3,j*3,0) == 1){ // check if 0 would be a valid number for that grid. If it is, there is no 0, meaning the grid has been filled
                solvedSquares++;            //so iterate solvedSquares by one
            }
            if (solvedSquares == 3){        //if there are three solvedSquares
                return 1;                   //return 1, meaning the puzzle is partially solved
            }
        }
        
    }                                       //if there are less than 3 solved squares, return 0
    if (solvedSquares < 3){
        return 0;
    }
    else return 1;                          //I think this is unnecessary given the return on line 129, but it doesn't hurt to be thorough
}

int checkSolved(){
    //this is similar to partialSolved() but for a complete solution, rather than a partial solution
    int i,j;
    for (i = 0;i<9;i++){    //for each row,
        for (j=0;j<9;j++){  //and each cell in that row
            if (sudokuCells[i][j] == 0){    //if it's unfilled, then the puzzle has not been solved
                return 0;                   //so return 0
            }
        }
    }
    return 1;   //otherwise, there are no unsolved cells, so the puzzle is complete
}



int solveSudoku(int row, int col) {
    // solveSudoku(row,col) takes in a certain cell and tests numbers 1 to 9 to see if it's a valid move for a possible solution
    // This is a kind of modified maze search algorithm which I learned about in previous classes. It allows for a kind of heuristic testing,
    // where a human would be able to look ahead a few moves to see if a certain number would lead to a solution. In the maze search, any given turn 
    // could or could not lead to a solution - each possible turn is then continued until a dead end is hit, then it recursivly retraces its steps until
    // the next possibility is hasn't tried. In this, each possible number for a cell (one that isn't used in that row, column, and grid) is tested
    // for all further possibilities until a complete puzzle has been put together


    // This is our base case, if we're on our last row and past the last column, then the solution has been found
    if (row == 8 && col > 8)
        return 1;

    // If we've iterated over all columns in this row, then move to the next row and restart at the first column (0).
    if (col > 8){
        row++;
        col = 0;
    }
    // If the current cell already has a number other than 0, move to the next column
    if (sudokuCells[row][col] != 0){
        return solveSudoku(row, ++col);
    }

    // Loop over each number from 1 - 9, and test if it's a legal choice for the given cell (row,col)
    int num;
    for (num = 1; num < 10; num++) {
        // If the current num is unused in the current row, column, and square, then continue to test further possibilities in the next cell
        if (rowCheck(row,num)==1 && columnCheck(col,num) == 1 && gridCheck(row,col,num) == 1){
            // Insert the number into the current cell, 
            sudokuCells[row][col] = num;
            // and test all future possibilities.
            if (solveSudoku(row, col + 1) == 1){ // if it (recursively) returns true, 
                return 1;   // then return true for this num in this cell, meaning it's correct
            }
        }
        // otherwise, it's an invalid choice, reset this cell to 0
        sudokuCells[row][col] = 0;
    }
    // if this returns 0, there is no correct solution for the given sudoku (in this recursive step, or at all)
    return 0;
}

int partialSolveSudoku(int row, int col) {
    // this is the same algorithm as solveSudoku(row,col), just modified to only solve the first three squares. 
    if (partialSolved() == 1)   //so our base case is now partialSolved(), which returns 1 when there are three solved squares
        return 1;
    // otherwise, continue solving like normal
    // iterate to the next row if we've reached past the last column
    if (col > 8){
        row++;
        col = 0;
    }
    
    // iterate to the next cell if this cell already has a value
    if (sudokuCells[row][col] != 0){
        return partialSolveSudoku(row, ++col);
    }
    // otherwise, test all legal numbers in this cell
    int num;
    for (num=1; num < 10; num++) {
        //if it's a legal choice for this cell, test future possibilities
        if (rowCheck(row,num)==1 && columnCheck(col,num) == 1 && gridCheck(row,col,num) == 1){
            sudokuCells[row][col] = num;
            if (partialSolveSudoku(row, col + 1)==1)
                return 1;
        }
        //if it's not a legal choice, reset it and move on
        sudokuCells[row][col] = 0;
    }
    //otherwise, return 0 for no solution
    return 0;
}
int main(){

    stepOne();
    stepTwo();
    stepThree();

}
