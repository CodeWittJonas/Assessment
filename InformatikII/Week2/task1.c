#include <stdio.h>
#include <iso646.h>

int lcm(int x, int y, int result) {
    if (x == 0 || y == 0) {
        return 0;
    }
    if (x == y) {
        return result = x;
    }
    if (x < y) {
        result += y;
    } else if (x > y) {
        result += x;
    }
    if (result % x == 0 && result % y == 0) {
        return result;
    } else {
        return lcm(x, y, result);
    }
}

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

int lcmWithGcd(int x, int y) {
    return (x * y) / gcd(x, y);
}

int main() {

    printf("%d\n", gcd(4, 4));
    printf("%d\n", lcmWithGcd(8, 22));
    printf("%d\n", lcm(8, 22, 0));
}

