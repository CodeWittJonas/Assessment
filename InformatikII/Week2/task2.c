#include <stdio.h>

void drawTriangle(int levels, int curLevel) {
    int numSpaces = curLevel - 1;
    int numStars = (levels - curLevel) * 2 + 1;

    if (curLevel > 0) {
        for (int i = 0; i < numSpaces; ++i) {
            printf(" ");
        }
        for (int j = 0; j < numStars; ++j) {
            printf("*");
        }
        printf("\n");
        drawTriangle(levels, (curLevel - 1));
    } else {
        return;
    }
}


int main(){
    int levels;
    printf("Enter height of Triangle: ");
    scanf("%d", &levels);
    drawTriangle(levels, levels);
}