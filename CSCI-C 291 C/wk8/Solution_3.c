#include <stdio.h>
#include <stdlib.h>

int main(void){
    int i,j;
    char *aPtr = (char*)malloc(sizeof(char)*20);
    printf("Question A:\n");
    for (i=0;i<20;i++){
        *(aPtr + i) = (i + 65);
        printf("%c", *(aPtr + i));
    }
    int rows = 5;
    int columns = 5;

    char **bPtr = (char**)malloc(rows*sizeof(char*));
    for (i = 0;i<rows;i++){
        *(bPtr+i) = (char*)malloc(columns*sizeof(char*));
    }
    printf("\n\nQuestion B:");
    for (i=0;i<rows;i++){
        printf("\n");
        for(j=0;j<columns;j++){
            *(*(bPtr+i)+j) = ((i*rows)+j+65);
            printf("%c ", *(*(bPtr+i)+j));
        }
    }
    printf("\n\nQuestion C:");
    char *cPtr = (char*)malloc((rows*columns)* sizeof(char));
    for(i=0;i<rows;i++){
        printf("\n");
        for(j=0;j<columns;j++){
            *(cPtr+(i*rows)+j)= ((i*rows)+j)+65;
            printf("%c ", *(cPtr + (i*rows) + j));
        }
    }
    printf("\n");
    free(aPtr);
    free(bPtr);
    free(cPtr);
}
