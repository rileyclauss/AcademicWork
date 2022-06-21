#include <stdio.h>
#include <string.h>

int main(void){
    char str1[50];
    char str2[50];
    int len1, len2 = 0;
    printf("Enter string 1: \n");
    scanf("%s", &str1);
    printf("Enter string 2: \n");
    scanf("%s", &str2);
    for (int i = 0; i < 50; i++){
        if (str1[i] == '\0'){
            len1 = i;
            break;
        }
    }
    for (int i = 0; i < 50; i++){
        if (str2[i] == '\0'){
            len2 = i;
            break;
        }
    }

    printf("Length of string 1: %d\nLength of string 2: %d\nFirst string character by character:\n", len1, len2);
    for (int i = 0; i < len1+1; i++){
        printf("%c ", str1[i]);
    }
    printf("\n");
    strcat(str1,str2);

    printf("%s\n", str1);

}
