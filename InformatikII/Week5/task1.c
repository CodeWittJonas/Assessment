#include <stdio.h>


// helper Functions

int rightChild(int index) {
    return index * 2 + 2;
}

int leftChild(int index) {
    return index * 2 + 1;
}

int parent(int index) {
    return index / 2;
}

void swap(int A[], int firstElement, int secondElement) {
    int temp = A[firstElement];
    A[firstElement] = A[secondElement];
    A[secondElement] = temp;
}

void heapify(int A[], int i, int n) {

    int min = i;
    int left = leftChild(i);
    int right = rightChild(i);

    // check if child*ren exist*s
    if (n < right) {
        return;
    } else if (n < left) {
        if (A[i] > A[left]) {
            swap(A, i, left);
            return;
        }
    }

    // make comparison to put smallest element on top of tree
    if (A[left] < A[min]) {
        min = left;
    }
    if (A[right] < A[min]) {
        min = right;
    }
    swap(A, i, min);

    // recursively heapify again on child elements
    heapify(A, left, n);
    heapify(A, right, n);


}

// Task 1.1
void buildMinHeap(int A[], int n) {
    int m = n / 2;
    for (int i = m; i >= 0; i--) {
        heapify(A, i, n);
    }
}

// Task 1.2
void printHeap(int A[], int n) {
    int m = n / 2;
    for (int i = 0; i < m; i++) {

    }
}

// Task 1.3
void heapSort(int A[], int n) {
    int sorted = n;
    buildMinHeap(A, n);
    for (int i = n - 1; i > 0; i--) {
        swap(A, i, 0);
        sorted--;
        heapify(A, 0, sorted);
    }
}

// Task 1.4
void printArray(int A[], int n) {
    printf("\n");
    printf("|");
    for (int i = 0; i < n; ++i) {
        printf(" %d |", A[i]);
    }
}

int main() {

    int array[7] = {9, 8, 5, 7, 4, 1, 3};

    printArray(array, 7);

    buildMinHeap(array, 7);

    printArray(array, 7);

    swap(array, 0, 6);
    printArray(array, 7);
    buildMinHeap(array, 5);
    printArray(array, 7);

    return 0;
}