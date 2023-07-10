#include <stdio.h>
#include <stdlib.h>

struct Node {
    int key;
    struct Node* left;
    struct Node* right;
};

int isEmpty(struct Node* root) {
    return (root == NULL);
}

struct Node* newNode(int key) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->key = key;
    node->left = NULL;
    node->right = NULL;
    return node;
}

struct Node* insert(struct Node* node, int key) {
    if (node == NULL) {
        return newNode(key);
    }
    if (key < node->key) {
        node->left = insert(node->left, key);
    } else if (key > node->key) {
        node->right = insert(node->right, key);
    }
    return node;
}

struct Node* search(struct Node* root, int key) {
    if (root == NULL || root->key == key) {
        return root;
    }
    if (root->key < key) {
        return search(root->right, key);
    }
    return search(root->left, key);
}

struct Node* minValueNode(struct Node* node) {
    struct Node* current = node;
    while (current && current->left != NULL) {
        current = current->left;
    }
    return current;
}

struct Node* deleteNode(struct Node* root, int key) {
    if (root == NULL) {
        return root;
    }
    if (key < root->key) {
        root->left = deleteNode(root->left, key);
    } else if (key > root->key) {
        root->right = deleteNode(root->right, key);
    } else {
        if (root->left == NULL) {
            struct Node* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            struct Node* temp = root->left;
            free(root);
            return temp;
        }
        struct Node* temp = minValueNode(root->right);
        root->key = temp->key;
        root->right = deleteNode(root->right, temp->key);
    }
    return root;
}

void inorder(struct Node* node) {
    if (node != NULL) {
        inorder(node->left);
        printf("%d ", node->key);
        inorder(node->right);
    }
}

int isPerfect(struct Node* root, int depth, int level) {
    if (root == NULL)
        return 1;
    if (root->left == NULL && root->right == NULL)
        return (depth == level + 1);
    if (root->left == NULL || root->right == NULL)
        return 0;
    return isPerfect(root->left, depth, level + 1) && isPerfect(root->right, depth, level + 1);
}

int isFull(struct Node* root) {
    if (root == NULL)
        return 1;
    if (root->left == NULL && root->right == NULL)
        return 1;
    if (root->left != NULL && root->right != NULL)
        return isFull(root->left) && isFull(root->right);
    return 0;
}
// Function to find the depth of a node
int findDepth(struct Node* root, int data) {
    if (root == NULL) {
        return -1;
    }
    if (root->key == data) {
        return 0;
    }
    int depth;
    if (data < root->key) {
        depth = findDepth(root->left, data);
    } else {
        depth = findDepth(root->right, data);
    }
    if (depth == -1) {
        return -1;
    } else {
        return depth + 1;
    }
}

// Function to find the height of a node
int findHeight(struct Node* root, int data) {
    if (root == NULL) {
        return -1;
    }
    if (root->key == data) {
        return 0;
    }
    int leftHeight = findHeight(root->left, data);
    int rightHeight = findHeight(root->right, data);
    if (leftHeight > rightHeight) {
        return leftHeight + 1;
    } else {
        return rightHeight + 1;
    }
}

// Function to find the level of a node
int findLevel(struct Node* root, int data, int level) {
    if (root == NULL) {
        return -1;
    }
    if (root->key == data) {
        return level;
    }
    int leftLevel = findLevel(root->left, data, level + 1);
    if (leftLevel == -1) {
        return findLevel(root->right, data, level + 1);
    } else {
        return leftLevel;
    }
}
// Function to count the number of nodes in the tree
int countNodes(struct Node* root) {
    if (root == NULL) {
        return 0;
    }
    return 1 + countNodes(root->left) + countNodes(root->right);
}

// Function to calculate the height of a tree
int height(struct Node* root) {
    if (root == NULL) {
        return 0;
    }
    int leftHeight = height(root->left);
    int rightHeight = height(root->right);
    return (leftHeight > rightHeight) ? leftHeight + 1 : rightHeight + 1;
}

// Function to check if a tree is balanced or not
int isBalanced(struct Node* root) {
    if (root == NULL) {
        return 1;
    }
    int leftHeight = height(root->left);
    int rightHeight = height(root->right);
    if (abs(leftHeight - rightHeight) <= 1 && isBalanced(root->left) && isBalanced(root->right)) {
        return 1;
    }
    return 0;
}
void mirror(struct Node* node) {
    if (node == NULL)
        return;

    mirror(node->left);
    mirror(node->right);

    struct node* temp = node->left;
    node->left = node->right;
    node->right = temp;
}
int countLeafNodes(struct Node* root) {
    if (root == NULL) {
        return 0;
    } else if (root->left == NULL && root->right == NULL) {
        return 1;
    } else {
        return countLeafNodes(root->left) + countLeafNodes(root->right);
    }
}

// Function to count the number of internal nodes in the tree
int countInternalNodes(struct Node* root) {
    if (root == NULL || (root->left == NULL && root->right == NULL)) {
        return 0;
    } else {
        return 1 + countInternalNodes(root->left) + countInternalNodes(root->right);
    }
}

// Function to perform pre-order traversal of the tree
void preOrder(struct Node* root) {
    if (root == NULL) {
        return;
    }
    printf("%d ", root->data);
    preOrder(root->left);
    preOrder(root->right);
}

// Function to perform in-order traversal of the tree
void inOrder(struct Node* root) {
    if (root == NULL) {
        return;
    }
    inOrder(root->left);
    printf("%d ", root->key);
    inOrder(root->right);
}

// Function to perform post-order traversal of the tree
void postOrder(struct Node* root) {
    if (root == NULL) {
        return;
    }
    postOrder(root->left);
    postOrder(root->right);
    printf("%d ", root->key);
}
// Function for non-recursive inorder traversal of a binary search tree
void inorderTraversal(struct Node* root) {
    struct node* stack[100];
    int top = -1;
    struct node* curr = root;
    
    while (curr != NULL || top != -1) {
        while (curr != NULL) {
            stack[++top] = curr;
            curr = curr->left;
        }
        curr = stack[top--];
        printf("%d ", curr->val);
        curr = curr->right;
    }
}

// Function for non-recursive preorder traversal of a binary search tree
void preorderTraversal(struct node* root) {
    if (root == NULL) {
        return;
    }
    
    struct node* stack[100];
    int top = -1;
    stack[++top] = root;
    
    while (top != -1) {
        struct node* curr = stack[top--];
        printf("%d ", curr->val);
        if (curr->right != NULL) {
            stack[++top] = curr->right;
        }
        if (curr->left != NULL) {
            stack[++top] = curr->left;
        }
    }
}

// Function for non-recursive postorder traversal of a binary search tree
void postorderTraversal(struct node* root) {
    if (root == NULL) {
        return;
    }
    
    struct node* stack1[100];
    struct node* stack2[100];
    int top1 = -1, top2 = -1;
    stack1[++top1] = root;
    
    while (top1 != -1) {
        struct node* curr = stack1[top1--];
        stack2[++top2] = curr;
        if (curr->left != NULL) {
            stack1[++top1] = curr->left;
        }
        if (curr->right != NULL) {
            stack1[++top1] = curr->right;
        }
    }
    
    while (top2 != -1) {
        struct node* curr = stack2[top2--];
        printf("%d ", curr->val);
    }
}

node* destroyTree(BST t){
    if(t==NULL) return NULL;
    if(t!=NULL){
        destroyTree(t -> right);
        destroyTree(t -> left);
        free(t);
    }
    return NULL;
}