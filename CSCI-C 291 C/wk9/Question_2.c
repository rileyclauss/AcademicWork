


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

//Written by Riley Clauss, 12/3/2021

struct word{
    char characters[20];
    int occurence;
};
int isVowel(char ch);

int main(){

    FILE *fPtr;
    if((fPtr = fopen("data-1.txt", "r+")) == NULL){
        printf("Error in opening file.\n");
        return 0;
    }    
    char ch[300];
    struct word dictionary[300];
    int lineSize = 100;
    int i = 0, wordsCounted = 0, newWord = 1;
    int countWords = 0, countLines=1,countVowels=0;

    while(fscanf(fPtr, " %19s", ch) == 1){
        countWords++;
        newWord = 1;
        for (i=0;i<wordsCounted;i++){
            if (strcasecmp(ch, dictionary[i].characters) == 0){
                dictionary[i].occurence++;
                newWord = 0;
            }
        }
        if (newWord == 1){
            strcpy(dictionary[wordsCounted].characters,ch);
            dictionary[wordsCounted].occurence = 1;
            wordsCounted++;
        }
        
    }
    rewind(fPtr);
    while(fgets(ch, 300, fPtr) != NULL){
        countLines++;
    }
    printf("Occurence of all words: \n");
    for (i=0;i<wordsCounted;i++){
        printf("%s: %d\n", dictionary[i].characters, dictionary[i].occurence);
        if (isVowel(dictionary[i].characters[0])){
            countVowels++;
        }
    }
    

    printf("Number of words: %d\nNumber of lines: %d\nNumber of words beginning with a vowel: %d\n",countWords,countLines,countVowels);


}

int isVowel(char c){
    c = toupper(c);
    return (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
}
