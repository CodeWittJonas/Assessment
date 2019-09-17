#include <stdio.h>
#include <malloc.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode *createNode(int val) {
    struct TreeNode *newNode = (struct TreeNode *) malloc(sizeof(struct TreeNode));
    if (newNode == NULL) {
        printf("Out of memory!");
        exit(1);
    }

    newNode->val = val;
    newNode->right = NULL;
    newNode->left = NULL;
    return newNode;
}


void insert(struct TreeNode *root, int val) {
    struct TreeNode *newNode = createNode(val);
    struct TreeNode *temp;
    if (root->left == NULL && root->right == NULL){
        if (root->val > val){
            root->left = newNode;
            return;
        } else {
            root->right = newNode;
            return;
        }
    }
}

void printInorder(struct TreeNode *root) {
    if (root->left == NULL && root->right != NULL) {
        printf("%d\n", root->val);
        printInorder(root->right);
    } else if (root->left != NULL) {
        printInorder(root->left);
    } else {
        printf("%d\n", root->val);
        return;
    }
}


int main() {

    struct TreeNode *root = createNode(15);
    printInorder(root);
    insert(root, 20);
    printInorder(root);

}
