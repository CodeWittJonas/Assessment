#include <stdio.h>

void towersOfHanoi(int n, char start, char end, char aux) {
    if (n == 1) {
        printf("\nMove 1 from %c to %c", start, end);
        return;
    }
    towersOfHanoi(n - 1, start, aux, end);
    printf("\nMove %d from %c to %c", n, start, end);
    towersOfHanoi(n - 1, aux, end, start);
}

int main() {
    towersOfHanoi(6, 'A', 'C', 'B');

    return 0;
}