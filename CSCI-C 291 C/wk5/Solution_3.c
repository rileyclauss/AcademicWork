#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

int const LENGTH = 50;

bool compare(char[*], char[*]);
int getLen(char[*]);
int getSum(char[*]);
bool swapCheck(char[*], char[*]);

int main(void){

    char str1[LENGTH];       //initialize the two strings
    char str2[LENGTH];
    printf("Enter your first string: ");
    scanf("%s", str1);
    printf("Enter your second string: ");
    scanf("%s", str2);
    printf("These are %sconvertible.\n", compare(str1, str2) ? "" : "not ");   //ternary operator to print whether or not the strings are convertibile
}

bool compare(char str1[LENGTH], char str2[LENGTH]){   //Main engine for checking the different operations
    if (getLen(str1) != getLen(str2))                 //If they are of different lengths, they are not convertible
        return false;
    for (int i = 0;i<getLen(str1);i++){               //cleanse the input to lowercase letters
        str1[i] = tolower(str1[i]);
        str2[i] = tolower(str2[i]);
    }

    if (getSum(str1) == getSum(str2)){             //This is operation 1: if we can swap as much as we want,              
        return true;                               //then the order of the chars doesn't matter, so adding all their values together
    }                                              //will tell us if any amount of swapping would be useful.
    if (swapCheck(str1,str2)){                     //This is operation 2, explained below.
        return true;
    }
    return false;  //If operation 1 and 2 fail, it is not convertibile.
}

int getLen(char str[LENGTH]){               //this function finds the endline character in the string
    int strLen = 0;                         //and returns the length. This is useful for forloops, which are used extensively.
    for (int i = LENGTH - 1; i >= 0; i--){  //Start at the end, find the first endline character.
        if (str[i] - 0 == 0)
            strLen = i;
    }
    return strLen;
}

int getSum(char str[LENGTH])
{
    int sum = 0;
    for (int i = 0; i < getLen(str); i++){  //This is operation 1, add the values of every character together
        sum += str[i];                      //If they are equal, then swapping positions will yield the same string, as there are the same 
    }                                       //letters in each string.
    return sum;
}

bool swapCheck(char str1[LENGTH], char str2[LENGTH]){
    /*
        This is operation 2. By switching the value of two characters including their position (which we already know is irrelevant to convertibility)
        we are essentially analyzing the frequency that the two characters take; if AAAAB and BBBBA are convertibile, it's because
        the first string has 4 As and 1 B, and the second string has 4 Bs and 1 A. This function finds the frequency table
        for both strings; if they are the same then some amount of switching will yield the same string.
    */

    int freq1[26]={0};                                  //This is an array of each letter in the alphabet's frequency for the first string
    int freq2[26]={0};                                  //And this is the frequency array for the second string
    bool used1[26] = {false};                           //These two arrays ensure that the same letters are being used, regardless of frequency
    bool used2[26] = {false};                           //While aaabbc and hhhggy have the same frequency, they cannot be swapped to
    char freqC1[26] = {};                               //This char array takes the non-zero integers from freq1[] to make comparison easier later on
    int uChars1 = 0;                                    //and this is the number of unique characters in the string, the length of freqC1[]
    char freqC2[26] = {};                               //This is the same as freqC1[] for string 2
    int uChars2 = 0;                                    //and the same as uChars1 for string 2

    for (int i = 0; i < getLen(str1); i++){             //This for loop iterates over both strings, which we already know are the same length
        freq1[str1[i] - 97]++;                          //and adds to the frequency table for their respective string. -97 is because we already know that
        freq2[str2[i] - 97]++;                          //each char is lowercase, so -97 allows us to use freq1[0] for 'a', freq1[1] for 'b', and so on.
        used1[str1[i] - 97] = true;                     //so the string 'aaabbczz' would yield freq1 = {3, 2, 1, 0,0,...0,2};
        used2[str2[i] - 97] = true;
    }
    
    for (int i = 0; i < 26; i++){                       //This forloop converts the frequency table from integers, including 0, to usable int-as-character tables
        if (used1[i] != used2[i]){                      //if one string has a letter that is not used by the other string, they are not convertibile
            return false;
        }
        if (freq1[i] > 0){                              //If a character was used, the frequency is added to the freqC1/C2 arary and 
            freqC1[uChars1] = freq1[i] + 97;            //the number of unique characters is incremented.
            uChars1++;                                  //If the number of unique characters is different for the strings, they are not convertible
        }
        if (freq2[i] > 0){                              //Same as above for string 2.
            freqC2[uChars2] = freq2[i] + 97;            //so aaabbczz as above would yield freqC1 = {'3','2','1','2'} -- only the frequency of
            uChars2++;                                  //used letters are added
        }
    }
    if (uChars1 != uChars2){                            //If there are an unequal number of unique characters, no amount of switching
        return false;                                   //will yield the same string, and is thus not convertibile
    }

    char temp;                                          //Below is an algorithim to sort both arrays into reverse-numerical order,
    for (int i = 0; i < uChars1 - 1; i++){              //so aaabbczz would change from {'3','2','1','2'} to {'3','2','2','1'}. 
        for (int j = i + 1; j < uChars1; j++){          //compare every value to those after it
            if (freqC1[i] > freqC1[j]){                 //and switch if they are larger
                temp = freqC1[i];
                freqC1[i] = freqC1[j];
                freqC1[j] = temp;
            }
            if (freqC2[i] > freqC2[j]){
                temp = freqC2[i];
                freqC2[i] = freqC2[j];
                freqC2[j] = temp;
            }
        }
    }
    return strcmp(freqC1,freqC2) == 0 ? true : false; //finally, the two character frequency strings, in order, are compared; if they are         
}                                                     //equal, then some swapping will work and they are convertibile
