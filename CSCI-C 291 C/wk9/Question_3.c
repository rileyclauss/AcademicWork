
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Written by Riley Clauss, 12/3/2021

int main(){

    FILE *file1;
    if((file1 = fopen("q31.txt", "w+")) == NULL){
        printf("Error in opening file.\n");
        return 0;
    }   
    FILE *file2;
    if((file2 = fopen("q32.txt", "w+")) == NULL){
        printf("Error in opening file.\n");
        return 0;
    }

    fprintf(file1, "This is\n\na collection of\ndummy words\nin\n\n\nno particular order\n");
    fprintf(file2, "\"We should start back,\" Gared urged as the woods began to grow dark around them.\n\"The wildlings are dead.\"\n\"Do the dead frighten you?\" Ser Waymar Royce asked with just the hint of a smile.\nGared did not rise to the bait. He was an old man, past fifty, and he had seen the lordlings come and go. \"Dead is dead,\" he said. \"We have no business with the dead.\"\n\"Are they dead?\" Royce asked softly. \"What proof have we?\"\n\"Will saw them,\" Gared said.");

    rewind(file1);
    rewind(file2);
    char ch[100], curr, prev;
    int i = 0;
    while((curr = fgetc(file1)) != -1){
        if (curr != '\n' && curr != EOF){
            ch[i++] = curr;
        }
        else if (curr == '\n'){
            if(prev != '\n'){
                ch[i++] = curr;
            }
        }
        prev = curr;
    }
    fclose(file1);
    file1 = fopen("q31.txt", "w+");
    fprintf(file1, ch);
    fclose(file1);
    file1 = fopen("q31.txt", "a+");
    while (!feof(file2)) {
        fgets(ch, 99, file2);
        fprintf(file1, "%s", ch);
    }

}
