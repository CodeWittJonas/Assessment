#include <stdio.h>

int gcd(int x, int y) {
    if (x == y) {
        return x;
    }
    if (x > y) {
        return gcd(y, (x - y));
    } else {
        return gcd(x, (y - x));
    }
}

int lcm(int x, int y) {
    return (x * y) / gcd(x, y);
}

int main() {

    printf("%d\n", gcd(4, 4));
    printf("%d\n", lcm(8, 32));
}

