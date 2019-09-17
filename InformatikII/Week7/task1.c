#include <stdio.h>
#include <malloc.h>

#define INITIAL_STACK_SIZE 5

typedef struct Stack {
    int *elements;
    int size;
    int count;
} stack;

struct Stack* initializeStack() {
    struct Stack* stack;
    stack = malloc(sizeof(struct Stack));
    stack->size = INITIAL_STACK_SIZE;
    stack->count = -1;
    stack->elements = malloc(sizeof(int)* INITIAL_STACK_SIZE);
    return stack;
}

int isEmpty(struct Stack *stack) {
    if (stack->size == 0) {
        return 1;
    } else {
        return 0;
    }
}

int push(struct Stack *stack, int value) {
    stack->count++;
    if (stack->size == stack->count){
        stack->elements = realloc(stack->elements, sizeof(int)* (INITIAL_STACK_SIZE + 1));
    }
    int index = stack->count;
    stack->elements[index] = value;
    stack->size++;
    return stack->count;



}

int pop(struct Stack *stack) {
    if (isEmpty(stack) == 1){
        return -1;
    }
    int element;
    element = stack->elements[stack->count];
    stack->count--;
    stack->size--;
    return element;
}

void printStack(struct Stack *stack) {
    int index = stack->count;
    for (int i = 0; i < stack->size; ++i) {
        printf("\n%d", stack->elements[index]);
        if (index > 0){
            index--;
        } else{
            index = INITIAL_STACK_SIZE;
        }
    }
}

int main(){
    struct Stack* stackA = initializeStack();
    push(stackA, 5);
    push(stackA, 3);
    printStack(stackA);
    pop(stackA);
    push(stackA, 7);
    printStack(stackA);

    printf("\n%d", pop(stackA));
    printf("\n%d", pop(stackA));
    printf("\n%d", pop(stackA));

}