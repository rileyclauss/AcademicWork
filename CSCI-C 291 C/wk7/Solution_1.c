#include <stdio.h>
#include <stdlib.h>

struct Book {               //struct for the Books
    char bookTitle[20];
    char author[20];
    char genre[20];
    int bookId;
}; 

void library_books(struct Book * books[]); 

int main(void){
    struct Book * books[3];         //create an array of pointers to three books
    int i = 0;
    for (i;i<3;i++){
        books[i]=malloc(sizeof(struct Book));       //declare necessary memory space
        printf("Enter book %d title: ", i+1);
        gets(books[i]->bookTitle);
        printf("Enter book %d author: ", i+1);
        gets(books[i]->author);
        printf("Enter book %d genre: ", i+1);
        gets(books[i]->genre);
        printf("Enter book %d ID: ", i+1);
        scanf("%d", &books[i]->bookId);             //and input each data point
        getchar();                                  //this prevents over-reaching newline characters for the next run of the for loop
    }
    library_books(books);                           //then pass the array of pointers to the printing function
    free(books[0]);
    free(books[1]);
    free(books[2]);
}

void library_books(struct Book * books[]){
    int i = 0;  
    printf("%-20s|%-20s|%-20s|%-5s\n", "Title", "Author", "Genre", "ID");           //print the headers
    for (i;i<3;i++){                                                                //and print the books formatted
        printf("%20s|%20s|%20s|%5d\n",books[i]->bookTitle, books[i]->author, books[i]->genre, books[i]->bookId);
    } 
}
