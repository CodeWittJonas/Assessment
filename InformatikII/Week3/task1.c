#include <stdio.h>

int whatDoesItDo(int a[], int n){
    int counter = 0;
    int val = 1;
    int b[n];
    int c[n];
    for (int i = 0; i < n; i++){
        b[i] = a[i];
        c[i] = 0;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++){
            if (a[i] == b[j]){
                c[j] = val;
                val++;
            }
        }
        val = 1;
    }
    for (int i = 0; i < n; i++){
        if (c[i] == 2){
            counter++;
        }
    }
    return counter;
}

int main(){
    int a[10] = {5, 6, 5, 6, 6, 4, 4};
    int result = whatDoesItDo(a, 7);
    printf("%d", result);
    return 0;
}