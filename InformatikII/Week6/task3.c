#include <stdio.h>
#include <malloc.h>

#define ROWS 5
#define COLS 4


int main(){

    int rows = ROWS;
    int cols = COLS;
    int count = 0;
    int ** matrix;
    int ** transpose;

    matrix = malloc(sizeof(int*)*rows);

    for (int i = 0; i < rows; ++i) {
        matrix[i] = malloc(sizeof(int));
    }


    // print matrix
    printf("\nMatrix: \n");
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < cols; ++j) {
            matrix[i][j] = ++count;
            printf("| %d", matrix[i][j]);
        }
        printf("\n");
    }

    printf("\n");

    // generate space for transpose
    transpose = malloc(sizeof(int *) * cols);

    for (int i = 0; i < cols; i++){
        transpose[i] = malloc(sizeof(int));
    }

    // populate transpose so that cols are rows
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            transpose[j][i] = matrix[i][j];
        }
    }

    // print transpose
    printf("\nTranspose of original Matrix: \n");
    for (int i = 0; i < cols; i++){
        for (int j = 0; j < rows; ++j) {
            printf("| %d", transpose[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < rows; i++){
        free(matrix[i]);
    }
    free(matrix);

    for (int k = 0; k < cols; ++k) {
        free(transpose[k]);
    }
    free(transpose);
 
    return 0;
}