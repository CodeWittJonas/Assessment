#include <stdio.h>

int lcmWithGcd(int x, int y) {
    int max;
    int min;
    if (x > y) {
        max = x;
        min = y;
    } else {
        max = y;
        min = x;
    }
    for (int i = 1; i <= max; ++i) {
        if ((i * min) % max == 0) {
            return i * min;
        }
    }
}

int gcd(int x, int y) {
    int zwischenresultat;
    if (x > y) {
        zwischenresultat = x % y;
        if (zwischenresultat == 0) {
            return y;
        } else if (zwischenresultat == 1) {
            return 1;
        } else {
            return gcd(y, zwischenresultat);
        }
    } else{
        zwischenresultat = y % x;
        if (zwischenresultat == 0) {
            return x;
        } else if (zwischenresultat == 1) {
            return 1;
        } else {
            return gcd(x, zwischenresultat);
        }
    }
}

void drawTriangle(int levels, int level){
    if (level > levels){
        return;
    }


}

int main() {

    printf("%d\n", lcmWithGcd(3, 4));
    printf("%d\n", lcmWithGcd(16, 12));
    printf("%d\n", gcd(15, 12));


}
