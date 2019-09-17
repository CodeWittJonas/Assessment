#include <stdio.h>
#include <malloc.h>

struct node{
    int val;
    struct node* next;
};

struct list {
    struct node* head;
};

struct list* init(){
    struct list* listA = malloc(sizeof(struct list));
    listA->head = NULL;
    return listA;
}

int size(struct list *listA){
    int counter = 0;
    struct node* currentElement = listA->head;
    while (currentElement != NULL){
        counter++;
        currentElement = currentElement->next;
    }
    return counter;
}

void appendAtTail(struct list *listA, int val){
    struct node newElement;
    newElement.val = val;
    newElement.next = NULL;

    struct node* currentElement = listA->head;
    while (currentElement->next != NULL){
        currentElement = currentElement->next;
    }
    *currentElement->next = newElement;

}

int main(){
    int i;
    int *p;

    i = 10;
    p = &i;

    printf("\n%p", p);
    printf("\n%d", *p);

    return 0;
}