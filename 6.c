// This problem was asked by Google.

// An XOR linked list is a more memory 
// efficient doubly linked list. Instead 
// of each node holding next and prev fields, 
// it holds a field named both, which is an 
// XOR of the next node and the previous node. 
// Implement an XOR linked list; it has an 
// add(element) which adds the element to the 
// end, and a get(index) which returns the node 
// at index.

// If using a language that has no pointers 
// (such as Python), you can assume you have 
// access to get_pointer and dereference_pointer 
// functions that converts between nodes and 
// memory addresses.

#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

// Assume elements contain int, but any type is
// fine. Also, I would generally write a function
// to free the list, but nah

typedef struct node {
    int val;
    long xnp;
} Node;

void add(Node** list, int val){
    Node* new = malloc(sizeof(Node));
    new->val = val;
    //printf("new_ptr = %p\n", (void*)new);

    if(*list == NULL){
        new->xnp = 0;
        *list = new;
        //printf("%p->NULL\n", (void*)new);
        return;
    }

    long prev_ptr = 0;
    Node* cur = *list;
    printf("%d->", cur->val); 
    //printf("prev_ptr = %p\n", (void*)prev_ptr);
    while((prev_ptr ^ cur->xnp) != 0){
        //printf("%d\n", (prev_ptr ^ cur->xnp) != 0);
        long cur_ptr = (long) cur;
        cur = (Node*) (prev_ptr ^ cur->xnp);
        prev_ptr = cur_ptr;
        printf("%d->", cur->val);
        //printf("prev_ptr = %p\n", (void*)prev_ptr);
        //printf("cur->xnp = %p\n", (void*)cur->xnp);
    }

    cur->xnp = prev_ptr ^ ((long) new);
    new->xnp = (long) cur ^ 0;
    printf("%d->NULL\n", new->val);
    //printf("cur->xnp = %p\n", (void*)cur->xnp);
}

Node* get(Node** list, int index){
    if (*list == NULL){ return NULL; }

    long prev_ptr = 0;
    Node* cur = *list;
    for(int i = 0; i < index; i++){
        if ((prev_ptr ^ cur->xnp) == 0) { return NULL; }
        long cur_ptr = (long) cur;
        cur = (Node*) (prev_ptr ^ cur->xnp);
        prev_ptr = cur_ptr;
    }
    return cur;
}

int main(){
    Node* list = NULL;
    add(&list, 0);
    //printf("%p\n", (void*)list);
    printf("1\n");
    add(&list, 1);
    printf("2\n");
    add(&list, 2);
    printf("4\n");
    add(&list, 4);
    printf("%d\n", get(&list, 3)->val);

    return EXIT_SUCCESS;
}
