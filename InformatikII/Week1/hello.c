#include <stdio.h>

#define n 100


void convertChar(char input[]) {

    for (int i = 0; i < 4; ++i){

        if (123 > input[i] > 96) {
            int ascii = input[i];
            ascii += 32;
            char conv = ascii;
            input[i] = conv;
        } else if (64 < input[i] < 91) {
            int ascii = input[i];
            ascii -= 32;
            char conv = ascii;
            input[i] = conv;
        }
        i++;
    }
}

void taskFour(){
    int a[20], b[20];
    int result[40];

    printf("Values of A separated by spaces (non-number to stop): ");
    scanf("%d", &a);

    printf("Values of B separated by spaces (non-number to stop): ");
    scanf("%d", &b);

    int j = 0;
    int k = 0;
    for (int i = 0; i < 40; ++i) {

        if (a[j] > b[k]){
            result[i] = a[j];
            j++;
        }else if(a[j] < b[k]){
            result[i] = b[k];
            k++;
        } else if(a[j] == b[k]){
            result[i] = a[j];
            i++;
            j++;
            result[i] = b[k];
            k++;
        }

    }
    printf("Result: ");
    for (int l = 0; l < 40; ++l) {
        printf("%d ", result[l]);
    }
}

int main() {

    taskFour();

    return 0;
}