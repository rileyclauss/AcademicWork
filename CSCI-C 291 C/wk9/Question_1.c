#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

//Written by Riley Clauss, 12/3/2021


void enterDetails();
int searchStudent();
void displayFile();
void removeStudent();

int main(void) {
    int selection, running = 1;
    while (running == 1) {
        printf("     Student Information\n1. Enter student details\n2. Search for a student\n3. Display the file contents\n");
        printf("4. Remove a student\n5. Exit\nEnter your choice:\n");
        scanf(" %d", & selection);
        switch (selection) {
            case 1:
                enterDetails();
                break;
            case 2:
                searchStudent();
                break;
            case 3:
                displayFile();
                break;
            case 4:
                removeStudent();
                break;
            case 5:
                printf("\n");
                running = 0;
                break;
            default:
                printf("Input not recognized, please try again.\n");
                break;
        }
    }
}
void enterDetails(){

    char name[20], course[10];
    int idNum;
    printf("Enter the student's details:\nStudent name: ");
    scanf("%s", name);
    printf("Enter student ID: ");
    scanf("%d", &idNum);
    printf("Course taken: ");
    scanf("%s", course);
    FILE *filePtr;
    if((filePtr = fopen("studentInfo.txt", "a+")) == NULL){
        printf("Unable to create file.\n");
        abort();
    }
    fprintf(filePtr, "%s,%d,%s\n", name, idNum, course);
    printf("Student details saved.\n");
    fclose(filePtr);
}
int searchStudent(){
    FILE *filePtr;
    if ((filePtr = fopen("studentInfo.txt", "r")) == NULL){
        printf("Unable to open file.");
        return -1;
    }
    rewind(filePtr);
    int searchId;
    printf("Enter the student's ID: ");
    scanf(" %d", &searchId);
    int id = 0,lineNum=0;
    char *p;
    char *line = (char*)malloc(sizeof(char)*30);
    while (fscanf(filePtr,"%s",line) != EOF){
        p=line;
        while(*p){
            if (isdigit(*p)){
                id = atoi(p);
                break;
            }
            else{
                p++;
            }
        }
        if(searchId == id){
            printf("%s\n", line);
            return lineNum;
        }
        lineNum++;
    }
    printf("The entered student ID does not exist in the database.\n");
    return -1;
}
void displayFile(){

    FILE *filePtr;
    if ((filePtr = fopen("studentInfo.txt", "r")) == NULL){
        printf("Unable to open file.");
        return;
    }
    rewind(filePtr);
    char line[30];
    while (fscanf(filePtr,"%s",line) != EOF){
        printf("%s\n", line);
    }
}
void removeStudent(){
    


}
